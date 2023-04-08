import argparse
import json
import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional

import influxdb_client
import pandas as pd


@dataclass
class Args:
    url: str
    org: str
    bucket: str
    token: str
    sensors: str

    def __repr__(self) -> str:
        return (
            f"Args(url='{self.url}',"
            + f" org='{self.org}'),"
            + f" sensors='{self.sensors}'"
        )


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-u",
        "--url",
        type=str,
        default="http://localhost:8086",
        help="provide the url of the influxdb database",
    )
    parser.add_argument(
        "-o",
        "--org",
        type=str,
        default="my-org",
        help="provide the org name of the influxdb database",
    )
    parser.add_argument(
        "-b",
        "--bucket",
        type=str,
        default="my-bucket",
        help="provide the bucket name of the influxdb database",
    )
    parser.add_argument(
        "-t",
        "--token",
        type=str,
        required=True,
        help="provide the token of the influxdb database",
    )
    parser.add_argument(
        "-s",
        "--sensors",
        type=str,
        required=True,
        help="provide the path to the jsonl file that contains all csv files",
    )

    args = parser.parse_args()

    return Args(
        url=args.url,
        org=args.org,
        bucket=args.bucket,
        token=args.token,
        sensors=args.sensors,
    )


@dataclass
class Sensor:
    path: str
    name: str
    tags: Dict[str, str]


def parse_sensor(
    root_path: str,
    path: str,
    name: str,
    tags: Optional[Dict[str, str]] = None,
) -> Sensor:
    return Sensor(
        path=os.path.join(root_path, path),
        name=name,
        tags=tags or dict(),
    )


def write_sensor(
    client: influxdb_client.InfluxDBClient,
    bucket: str,
    sensor: Sensor,
):
    df = pd.read_csv(sensor.path, index_col="time")

    for tag, tag_value in sensor.tags.items():
        df[tag] = tag_value

    tag_columns = list(sensor.tags.keys())

    with client.write_api() as write_api:
        write_api.write(
            bucket,
            record=df,
            data_frame_measurement_name=sensor.name,
            data_frame_tag_columns=tag_columns,
        )


def main(args: Args):
    logging.info(args)

    client = influxdb_client.InfluxDBClient(
        args.url,
        token=args.token,
        org=args.org,
    )

    sensors_path = Path(args.sensors)
    root_path = sensors_path.parent
    with open(sensors_path, "r", encoding="utf-8") as f:
        sensors = [parse_sensor(root_path, **json.loads(line)) for line in f]

    for sensor in sensors:
        write_sensor(client, args.bucket, sensor)


if __name__ == "__main__":
    logging.basicConfig(
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(os.getenv("LOG_FILE", "app.log")),
        ],
        level=os.getenv("LOG_LEVEL", logging.getLevelName(logging.DEBUG)),
        format="%(levelname)s: %(asctime)s \
            pid:%(process)s module:%(module)s %(message)s",
        datefmt="%d/%m/%y %H:%M:%S",
    )

    main(parse_args())

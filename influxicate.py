import argparse
import logging
import os
from dataclasses import dataclass

import influxdb_client


@dataclass
class Args:
    url: str
    org: str
    token: str

    def __repr__(self) -> str:
        return f"Args(url='{self.url}', org='{self.org}')"


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
        "-t",
        "--token",
        type=str,
        required=True,
        help="provide the token of the influxdb database",
    )

    args = parser.parse_args()

    return Args(
        url=args.url,
        org=args.org,
        token=args.token,
    )


def main(args: Args):
    logging.info(args)

    client = influxdb_client.InfluxDBClient(
        args.url,
        token=args.token,
        org=args.org,
    )

    print(client.health())


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

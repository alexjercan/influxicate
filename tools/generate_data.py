import numpy as np
import pandas as pd


def generate_csv(
    start="2023-01-01 00:00:00", end="2023-01-01 01:00:00", freq="S"
):
    time_series = pd.date_range(start=start, end=end, freq=freq)

    length = len(time_series)

    temp = np.random.uniform(20.0, 30.0, size=length).astype(np.float32)
    hum = np.random.uniform(0.0, 1.0, size=length).astype(np.float32)
    co = np.random.uniform(400, 500, size=length).astype(np.int32)

    df = pd.DataFrame(
        {"time": time_series, "temp": temp, "hum": hum, "co": co}
    )

    df["time"] = df["time"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S.%f"))

    return df


if __name__ == "__main__":
    generate_csv(
        start="2023-04-01 00:00:00", end="2023-04-01 00:00:01", freq="L"
    ).to_csv("example/home_kitchen_1K.csv", index=False)
    generate_csv(
        start="2023-04-02 00:00:00", end="2023-04-02 00:00:10", freq="L"
    ).to_csv("example/home_kitchen_10K.csv", index=False)
    generate_csv(
        start="2023-04-03 00:00:00", end="2023-04-03 00:01:40", freq="L"
    ).to_csv("example/home_kitchen_100K.csv", index=False)
    generate_csv(
        start="2023-04-01 00:00:00", end="2023-04-01 00:00:01", freq="L"
    ).to_csv("example/home_bedroom_1K.csv", index=False)
    generate_csv(
        start="2023-04-02 00:00:00", end="2023-04-02 00:00:10", freq="L"
    ).to_csv("example/home_bedroom_10K.csv", index=False)
    generate_csv(
        start="2023-04-03 00:00:00", end="2023-04-03 00:01:40", freq="L"
    ).to_csv("example/home_bedroom_100K.csv", index=False)
    generate_csv(
        start="2023-04-01 00:00:00", end="2023-04-01 00:00:01", freq="L"
    ).to_csv("example/store_hall_1K.csv", index=False)
    generate_csv(
        start="2023-04-02 00:00:00", end="2023-04-02 00:00:10", freq="L"
    ).to_csv("example/store_hall_10K.csv", index=False)
    generate_csv(
        start="2023-04-03 00:00:00", end="2023-04-03 00:01:40", freq="L"
    ).to_csv("example/store_hall_100K.csv", index=False)

# The jsonl file
# {"path": "home_kitchen_1K.csv", "name": "home", "tags": {"room": "kitchen"}}
# {"path": "home_kitchen_10K.csv", "name": "home", "tags": {"room": "kitchen"}}
# {"path": "home_kitchen_100K.csv", "name": "home", "tags": {"room": "kitchen"}}
# {"path": "home_bedroom_1K.csv", "name": "home", "tags": {"room": "bedroom"}}
# {"path": "home_bedroom_10K.csv", "name": "home", "tags": {"room": "bedroom"}}
# {"path": "home_bedroom_100K.csv", "name": "home", "tags": {"room": "bedroom"}}
# {"path": "store_hall_1K.csv", "name": "store", "tags": {"room": "hall"}}
# {"path": "store_hall_10K.csv", "name": "store", "tags": {"room": "hall"}}
# {"path": "store_hall_100K.csv", "name": "store", "tags": {"room": "hall"}}

# Influxicate

Tool used to add data to a influxdb database.

This tool is related to the [DRIPstack](https://github.com/alexjercan/DRIPstack) 🥶 chills

## Quickstart

You will need a influxdb database running on `localhost` port `8086` with an
organization named `my-org`. You will also need to create a token from the
database UI and pass it to the token argument.

```console
python influxicate.py --url http://localhost:8086 --org my-org --token $(INFLUXDB_TOKEN)
```

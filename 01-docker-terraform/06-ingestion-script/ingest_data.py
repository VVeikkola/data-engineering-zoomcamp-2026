import os
from pathlib import Path

import click
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL

# Load environment variables
env_path = Path(__file__).resolve()

for parent in env_path.parents:
    env_file = parent / ".env"

    if env_file.is_file():
        load_dotenv(env_file)
        break

# Data source
prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/"

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

@click.command()
@click.option("--year", default=2021, type=int)
@click.option("--month", default=1, type=int)
@click.option("--chunksize", default=100000, type=int)
@click.option("--target-table", default="yellow_taxi_data")
def run(year, month, chunksize, target_table):

    # Database configuration
    db_user = os.environ["POSTGRES_USER"]
    db_password = os.environ["POSTGRES_PASSWORD"]
    db_host = os.environ["POSTGRES_HOST"]
    db_port = int(os.environ["POSTGRES_PORT"])
    db_name = os.environ["POSTGRES_DB"]

    # Create database connection
    database_url = URL.create(
        drivername="postgresql+psycopg",
        username=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        database=db_name,
    )

    engine = create_engine(database_url)

    # Create CSV URL
    url = f"{prefix}yellow_tripdata_{year}-{month:02d}.csv.gz"

    # Read CSV in chunks
    df_iter = pd.read_csv(
        url,
        dtype=dtype,
        parse_dates=parse_dates,
        iterator=True,
        chunksize=chunksize,
    )

    first = True

    for df_chunk in df_iter:

        if first:
            df_chunk.head(0).to_sql(
                name=target_table,
                con=engine,
                if_exists="replace",
                index=False
            )

            first = False
            print("Table created")

        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists="append",
            index=False
        )

        print("Inserted:", len(df_chunk))

    engine.dispose()


if __name__ == "__main__":
    run()
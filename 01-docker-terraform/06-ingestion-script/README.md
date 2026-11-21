# 06 – Creating the Data Ingestion Script

## Overview

Converted the NYC Yellow Taxi data ingestion notebook into a reusable Python script that loads CSV data into PostgreSQL.

## Technologies

- Python
- pandas
- SQLAlchemy
- PostgreSQL
- Docker
- Click
- python-dotenv

## Implementation

The ingestion script:

1. Reads database credentials from environment variables.
2. Accepts command-line arguments using Click.
3. Downloads NYC Yellow Taxi trip data.
4. Processes the CSV file in configurable chunks.
5. Creates the target PostgreSQL table.
6. Inserts the data into the database.

## Usage

Make sure PostgreSQL is running and the required environment variables are configured.

```bash
uv run python ingest_data.py \
    --year=2021 \
    --month=1 \
    --chunksize=100000 \
    --target-table=yellow_taxi_test
```

## Validation

Successfully ingested the January 2021 NYC Yellow Taxi dataset containing 1,369,765 records.

A data quality check identified 24 records with pickup timestamps outside January 2021.

## Key Learnings

- Converting Jupyter notebooks into standalone Python scripts
- Building command-line interfaces with Click
- Parameterizing data ingestion workflows
- Reading configuration from environment variables
- Processing large datasets in chunks
- Loading and validating data in PostgreSQL
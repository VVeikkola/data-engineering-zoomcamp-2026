# 08 – Dockerizing the Ingestion Script

## Overview

In this exercise, I containerized a Python data ingestion pipeline using Docker.

The objective was to run the ingestion script inside a Docker container and connect it to a PostgreSQL database running in a separate container.

## Technologies

- Python 3.13
- Docker
- Docker Networks
- uv
- pandas
- SQLAlchemy
- Click
- PostgreSQL 18

## Architecture

```text
Docker Network: pg-network
│
├── PostgreSQL (de-postgres)
│   └── Database: ny_taxi
│
├── pgAdmin
│
└── Python Ingestion Container
    └── ingest_data.py
         │
         └── Inserts taxi data into PostgreSQL
```

## Implementation

1. Created a Dockerfile using Python 3.13.
2. Installed the project dependencies using uv.
3. Copied the ingestion script into the Docker image.
4. Configured the Docker entrypoint to execute the Python script.
5. Passed database configuration using environment variables.
6. Connected the ingestion container to PostgreSQL using a shared Docker network.
7. Processed NYC Yellow Taxi data in chunks of 100,000 rows.

## Building the Docker Image

Run from the project root:

```bash
docker build \
  -f 01-docker-terraform/08-dockerizing-ingestion/Dockerfile \
  -t taxi_ingest:v001 \
  .
```

## Running the Container

```bash
docker run --rm \
  --network=pg-network \
  --env-file .env \
  -e POSTGRES_HOST=de-postgres \
  taxi_ingest:v001 \
  --year=2021 \
  --month=1 \
  --chunksize=100000 \
  --target-table=yellow_taxi_docker
```

The `.env` file is kept outside version control.

## Data Validation

The January 2021 NYC Yellow Taxi dataset contains 1,369,765 records.

The following SQL query can be used to validate the Docker ingestion:

```sql
SELECT COUNT(*)
FROM yellow_taxi_docker;
```

Expected result: **1,369,765 rows**.

The ingested data can also be compared against the original table:

```sql
SELECT 'Original' AS source, COUNT(*) AS total_rows
FROM yellow_taxi_data

UNION ALL

SELECT 'Docker' AS source, COUNT(*) AS total_rows
FROM yellow_taxi_docker;
```

## Key Learnings

- Building Docker images for Python applications
- Understanding Dockerfile instructions
- Managing Python dependencies with uv
- Understanding the difference between images and containers
- Using Docker networks for container-to-container communication
- Passing configuration through environment variables
- Running parameterized data ingestion pipelines in Docker
- Debugging Python file paths inside containers
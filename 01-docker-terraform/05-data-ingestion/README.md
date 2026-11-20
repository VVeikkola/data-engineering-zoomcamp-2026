# 05 – NY Taxi Dataset and Data Ingestion

## Objective

Learn how to ingest real-world CSV data into PostgreSQL using Python, pandas, and SQLAlchemy.

## Technologies

- Python
- pandas
- SQLAlchemy
- PostgreSQL
- Docker
- Jupyter Notebook

## What I Learned

- Reading and exploring CSV datasets with pandas
- Inspecting DataFrame structures and data types
- Handling missing values using nullable data types
- Converting string columns into datetime objects
- Connecting Python applications to PostgreSQL using SQLAlchemy
- Generating SQL table schemas from pandas DataFrames
- Processing large datasets in chunks
- Inserting data into PostgreSQL using `to_sql()`
- Understanding the difference between `append` and `replace`
- Validating ingested data using SQL queries

## Practical Implementation

Built a data ingestion workflow that:

1. Reads NYC Yellow Taxi trip data from a compressed CSV file.
2. Defines explicit column data types.
3. Processes the dataset in batches of 100,000 rows.
4. Creates a PostgreSQL table.
5. Inserts each batch into the database.
6. Verifies the imported records using SQL queries.

## Key Takeaway

Chunk-based ingestion allows large datasets to be processed without loading the entire dataset into memory. Explicit data types and SQL validation help ensure that the ingested data is consistent and usable.

## Status

Completed ✅
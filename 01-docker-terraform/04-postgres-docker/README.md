# 04 – Running PostgreSQL with Docker

## Objective

Deploy a containerized PostgreSQL database and understand persistent storage, networking, and basic SQL operations.

## What I Learned

- Running PostgreSQL inside Docker
- Configuring containers using environment variables
- Docker port mapping
- Named volumes and bind mounts
- Persistent database storage
- Database connections using pgcli
- Development dependencies with uv
- Basic SQL operations
- Filtering data and using aggregate functions

## Practical Exercises

- Configured and launched a PostgreSQL 18 container.
- Verified port availability using the Linux `ss` command.
- Inspected Docker volumes.
- Connected to PostgreSQL using pgcli.
- Created database tables and inserted sample records.
- Retrieved, filtered, and counted records using SQL.
- Verified that database records persist after container removal and recreation.

## Key Takeaway

Docker provides an isolated and reproducible database environment, while named volumes allow database records to persist independently of the container lifecycle.

## Status

Completed ✅
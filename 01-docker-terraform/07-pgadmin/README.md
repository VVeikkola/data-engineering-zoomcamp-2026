# 07 – pgAdmin: Database Management Tool

## Overview

In this exercise, I set up pgAdmin using Docker and connected it to an existing PostgreSQL database.

The goal was to learn how Docker containers communicate through a shared network and how to manage PostgreSQL databases using a graphical interface.

## Technologies

- Docker
- Docker Networks
- Docker Volumes
- PostgreSQL 18
- pgAdmin 4
- SQL

## Architecture

The environment consists of two Docker containers connected through a shared Docker network.

```text
Ubuntu Host
    |
    | localhost:8085
    |
    v
pgAdmin Container
    |
    | pg-network
    |
    v
PostgreSQL Container (de-postgres)
    |
    v
ny_taxi Database
    |
    v
yellow_taxi_data
```

## Implementation

### 1. Create a Docker Network

Created a dedicated Docker network to enable communication between PostgreSQL and pgAdmin.

```bash
docker network create pg-network
```

### 2. Connect PostgreSQL to the Network

Connected the existing PostgreSQL container to the network without recreating the database.

```bash
docker network connect pg-network de-postgres
```

### 3. Run pgAdmin

Started pgAdmin in a separate Docker container.

```bash
docker run -d \
  --name pgadmin \
  --network pg-network \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="<local-development-password>" \
  -v pgadmin_data:/var/lib/pgadmin \
  -p 127.0.0.1:8085:80 \
  dpage/pgadmin4
```

The named Docker volume preserves pgAdmin settings between container restarts.

### 4. Connect to PostgreSQL

Opened pgAdmin at:

`http://localhost:8085`

Registered the PostgreSQL server using the following connection settings:

| Setting | Value |
|---|---|
| Server name | Local Docker |
| Host | de-postgres |
| Port | 5432 |
| Database | ny_taxi |
| Username | root |
| Password | Configured local database password |

The container name `de-postgres` is used instead of `localhost` because pgAdmin and PostgreSQL run in separate Docker containers.

### 5. Explore the Data

Used pgAdmin's Query Tool to explore the NYC Yellow Taxi dataset.

Example query:

```sql
SELECT *
FROM yellow_taxi_data
LIMIT 10;
```

Also practiced SQL aggregation by calculating the number of trips and average trip price for each payment type.

```sql
SELECT
    payment_type,
    COUNT(*) AS total_trips,
    AVG(total_amount) AS average_price
FROM yellow_taxi_data
GROUP BY payment_type
ORDER BY total_trips DESC;
```

## Results

- Successfully connected pgAdmin to PostgreSQL through a Docker network.
- Explored database tables using the graphical interface.
- Executed SQL queries against the NYC Yellow Taxi dataset.
- Analyzed payment methods, trip counts, and average trip prices.
- Verified access to the previously ingested dataset containing 1,369,765 records.

## Key Learnings

- Docker containers can communicate using a shared user-defined network.
- Container names can be used as hostnames within the same Docker network.
- `localhost` inside a container refers to that container, not the host machine.
- Docker volumes provide persistent storage for application settings.
- pgAdmin simplifies PostgreSQL database management and SQL exploration.
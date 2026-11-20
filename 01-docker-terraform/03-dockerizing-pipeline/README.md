# 03 – Dockerizing the Pipeline

## Objective

Containerize a Python data pipeline and build reproducible execution environments.

## What I Learned

- Dockerfile instructions: FROM, RUN, WORKDIR, COPY and ENTRYPOINT
- Docker build context
- Building and tagging Docker images
- Build-time and runtime differences
- Dependency management with pip and uv
- Reproducible builds using uv.lock
- Docker layer caching
- Passing command-line arguments to containers
- Persisting pipeline outputs using bind mounts

## Practical Exercises

- Built Docker images using pip and uv.
- Executed a parameterized Python data pipeline inside Docker containers.
- Generated Parquet files and persisted them outside the container.
- Tested Docker layer caching.

## Status

Completed ✅
FROM python:3.13.11-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set working directory
WORKDIR /code

# Add virtual environment to PATH
ENV PATH="/code/.venv/bin:$PATH"

# Copy dependencies
COPY pyproject.toml uv.lock ./

# Install Python dependencies 
RUN uv sync --locked --no-dev

# Copy ingestion script
COPY 01-docker-terraform/06-ingestion-script/ingest_data.py .

# Run ingestion script
ENTRYPOINT ["uv", "run", "--no-sync", "python", "ingest_data.py"]
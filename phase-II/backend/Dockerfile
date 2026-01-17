FROM python:3.11-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install additional dependencies for database connectivity
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the rest of the application
COPY . .

# Create a startup script to handle port mapping
RUN echo '#!/bin/bash\nset -e\nexport API_PORT=${PORT:-8000}\nalembic upgrade head\nexec uvicorn src.main:app --host 0.0.0.0 --port $API_PORT' > /app/start.sh
RUN chmod +x /app/start.sh

# Expose the port that the app runs on
EXPOSE 8000

# Run database migrations and start the application
CMD ["./start.sh"]
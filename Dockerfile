# Minimal API image (placeholder)
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "-m", "runner.cli", "train", "--dry-run", "--config", "conf/config.yaml"]

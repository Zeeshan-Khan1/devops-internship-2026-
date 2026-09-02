FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV APP_ENV=development
ENV PORT=5000
ENTRYPOINT ["python3", "app.py"]

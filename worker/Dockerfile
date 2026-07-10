FROM python:3.12-alpine
WORKDIR /app
RUN pip install --no-cache-dir redis==5.2.0
COPY worker.py .
CMD ["python", "worker.py"]

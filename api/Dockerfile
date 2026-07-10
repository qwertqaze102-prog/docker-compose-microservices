FROM python:3.12-alpine
WORKDIR /app
RUN pip install --no-cache-dir redis==5.2.0
COPY app.py .
EXPOSE 8000
CMD ["python", "app.py"]

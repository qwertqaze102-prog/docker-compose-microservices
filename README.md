# Docker Compose Microservices

**Stack skills:** `Docker` · `Nginx` · `Python` · `Redis` · `Linux` · `Git`

## Run
```bash
docker compose up -d --build
curl http://127.0.0.1:8088/api/health
curl -X POST http://127.0.0.1:8088/api/jobs -H "Content-Type: application/json" -d "{\"task\":\"ping\"}"
```

Services: Nginx :8088 → API → Redis queue → Worker

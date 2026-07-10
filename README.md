# Docker Compose Microservices Demo

Mini multi-service architecture:
- `api` — Python HTTP API
- `worker` — background job consumer (queue via redis)
- `redis` — broker
- `web` — nginx frontend proxy

```bash
docker compose up -d --build
curl http://localhost:8088/api/health
curl -X POST http://localhost:8088/api/jobs -d '{"task":"ping"}' -H 'Content-Type: application/json'
```

## Skills shown
multi-service design, networking, reverse proxy, queues, rebuildable local env

#!/usr/bin/env python3
import json
import os
import time
import redis

r = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://localhost:6379/0"), decode_responses=True)
print("worker started", flush=True)
while True:
    item = r.blpop("jobs", timeout=5)
    if not item:
        continue
    _, raw = item
    job = json.loads(raw)
    print(f"processing {job}", flush=True)
    time.sleep(0.4)
    print(f"done {job.get('task')}", flush=True)

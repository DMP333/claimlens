"""
Measures multi-user latency degradation against the RUNNING app.

Run it against the containerized app (docker compose up), NOT a local MPS uvicorn,
because the multi-user cost is the CPU inference serializing through the model lock,
and the container is CPU like the real deploy. On local MPS the numbers look milder
than they would in production.

Usage:  python measure_concurrency.py
"""

import json
import time
import urllib.request

BASE = "http://54.190.73.166:8000"
CLAIMS = [
    "vaccines cause autism",
    "the great wall of china is visible from space",
    "humans only use ten percent of their brains",
    "goldfish have a three second memory",
    "lightning never strikes the same place twice",
]


def submit(claim):
    data = json.dumps({"claim": claim}).encode()
    req = urllib.request.Request(
        BASE + "/verify", data=data, headers={"Content-Type": "application/json"}
    )
    return json.load(urllib.request.urlopen(req))["id"]


def status(job_id):
    try:
        return json.load(urllib.request.urlopen(BASE + "/verify/" + job_id))["status"]
    except Exception:
        return "ERR"


def run(n):
    print(f"\n=== {n} concurrent ===")
    start = time.perf_counter()
    # Distinct claims per slot: realistic load, avoids 5x-identical-query throttling.
    ids = [submit(CLAIMS[i % len(CLAIMS)]) for i in range(n)]
    done = {}
    while len(done) < n:
        for job_id in ids:
            if job_id in done:
                continue
            s = status(job_id)
            if s in ("done", "failed", "ERR"):
                done[job_id] = (time.perf_counter() - start, s)
        time.sleep(0.4)
    for i, job_id in enumerate(ids):
        secs, s = done[job_id]
        print(f"  claim {i + 1}: {secs:5.1f}s  {s}")
    slowest = max(secs for secs, _ in done.values())
    print(f"  slowest finisher: {slowest:.1f}s")


if __name__ == "__main__":
    for level in (1, 3, 5, 7, 9):
        run(level)
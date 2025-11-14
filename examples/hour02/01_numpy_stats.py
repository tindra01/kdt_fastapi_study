from typing import Iterable

import numpy as np
from fastapi import FastAPI

app = FastAPI(docs_url='/api/docs', openapi_url='/api/openapi.json')

def compute_stats(values: Iterable[float]) -> dict:
    arr = np.array(list(values), dtype=float)
    return {
        "count": int(arr.size),
        "mean": float(arr.mean()),
        "std": float(arr.std(ddof=0)),
    }

@app.get("/stats/basic")
def stats_endpoint() -> dict:
    sample = [2, 4, 4, 6, 9]
    return compute_stats(sample)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)
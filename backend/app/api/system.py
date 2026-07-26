from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/system", tags=["system"])

@router.get("/health")
def health():
    return {"status": "ok", "uptime": "ready"}

@router.get("/cache-metrics")
def cache_metrics():
    return {"cache_hits": 0, "cache_misses": 0, "cache_size": 0}

@router.post("/cache/clear", status_code=status.HTTP_200_OK)
def clear_cache():
    return {"status": "cleared"}

from fastapi import APIRouter, HTTPException

from .domain.schemas import ExtractRequest, ExtractResponse
from .config import settings
from .db import fetchrow



router = APIRouter(prefix="/v1")


@router.get("/healthz")
async def healthz():
    return {"ok": True}

@router.get("/engines")
async def engines():
     return {"default": settings.export_dir}

@router.get("/db-ping")
async def db_ping():
     row =  await fetchrow("SELECT 1 as ok")
     return dict(row)

@router.post("/extract", response_model=ExtractResponse)
async def extract(req: ExtractRequest):

    try:
        result = { 
            "book_id": req.book_id,
            "engine": "full" 
        }
        return ExtractResponse(**result)
    except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
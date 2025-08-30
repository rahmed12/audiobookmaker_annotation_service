from fastapi import APIRouter, HTTPException
from .domain.schemas import ExtractRequest, ExtractResponse

router = APIRouter(prefix="/v1")

@router.get("/healthz")
async def healthz():
    return {"ok": True}

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
        
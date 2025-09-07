from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager

from .api import router
from .db import init_pool, close_pool


@asynccontextmanager
async def lifespan(app: FastAPI):
     # db startup
     await init_pool()
     yield
     # db shutdown
     await close_pool()


app = FastAPI(title="annotationService", version="1.0.0", lifespan=lifespan)

app.include_router(router)


    
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8083, reload=True)
import asyncpg
from .config import settings
from typing import Optional, Sequence, Any

_pool: Optional[asyncpg.Pool] = None


async def init_pool():
    global _pool
    _pool = await asyncpg.create_pool(dsn=settings.pg_dsn, min_size=1, max_size=10)


async def close_pool():
    global _pool
    if _pool:
        await _pool.close()
        _pool = None

def pool() -> asyncpg.Pool:
    assert _pool is not None, "DB pool not initialized"
    return _pool

async def fetchrow(query: str, *args):
    async with pool().acquire() as conn:
        return await conn.fetchrow(query, *args)
# FastAPI app object is created and configured here. Kind of like main function in java
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.session import engine, Base
# Imported for its SIDE EFFECT only: defining the Verification class registers
# it on Base.metadata, which is what create_all reads. Without this import the
# table would silently not be created. (noqa: it is intentionally "unused".)
import app.db.models  # noqa: F401
from app.api.routes.claims import router as claims_router #importing router, which will handle requests appropriate to its given container


@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP: create any tables not already present. run_sync bridges the
    # synchronous create_all onto the async connection. Idempotent: existing
    # tables are left untouched (no data loss on restart).
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # SHUTDOWN: close the connection pool cleanly.
    await engine.dispose()


app = FastAPI(title="FalseClaimDetector", lifespan=lifespan)
#creates the instance and store it in app

app.include_router(claims_router) #allows us to use /verify, now our app object knows about /verify

#these are handlign different types of URL we handle
@app.get("/") #if someone sends a get request to '/', run the function directly below this
def root():
    return {"message": "FalseClaimDector is running"} #what gets returned in the json file

@app.get("/health")
def health():
    return {"status": "ok"}
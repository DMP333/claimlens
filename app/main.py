# FastAPI app object is created and configured here. Kind of like main function in java
from contextlib import asynccontextmanager
import os

from fastapi import FastAPI
from fastapi.responses import FileResponse

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


app = FastAPI(title="ClaimLens", lifespan=lifespan)
#creates the instance and store it in app

app.include_router(claims_router) #allows us to use /verify, now our app object knows about /verify

# Absolute path to the bundled single-file frontend (app/static/index.html).
# Built from __file__ so it resolves the same in local dev and in the container.
_FRONTEND = os.path.join(os.path.dirname(__file__), "static", "index.html")

#these are handlign different types of URL we handle
@app.get("/") #serve the web client (the human-facing page) at the root
def root():
    # The page's JavaScript calls /verify on this same origin, so the API and the
    # website share one server with no CORS setup. The API remains fully usable
    # on its own (curl/scripts hit /verify directly); the page is just another client.
    return FileResponse(_FRONTEND)

@app.get("/health")
def health():
    return {"status": "ok"}
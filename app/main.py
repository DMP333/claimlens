# FastAPI app object is created and configured here. Kind of like main function in java
from fastapi import FastAPI
#importing fastapi I have installed
from app.api.routes.claims import router as claims_router #importing router, which will handle requests appropriate to its given container

app = FastAPI(title="FalseClaimDetector")
#creates the instance and store it in app

app.include_router(claims_router) #allows us to use /verify, now our app object knows about /verify

#these are handlign different types of URL we handle
@app.get("/") #if someone sends a get request to '/', run the function directly below this
def root():
    return {"message": "FalseClaimDector is running"} #what gets returned in the json file

@app.get("/health")
def health():
    return {"status": "ok"}
from fastapi import APIRouter
from app.models import ClaimRequest, ClaimResponse, SourceResult
from app.services import claim_service

router = APIRouter() #object router holds info of everything below it
#@router make sure that endpoint and function gets stored under the object router

#fast api will automatically create ClaimRequest model automatically
@router.post("/verify", response_model=ClaimResponse) #claim response is a safety check.. this function should return this type in the end
def verify_claim(request: ClaimRequest) -> ClaimResponse:
    return claim_service.analyze_claim(request)

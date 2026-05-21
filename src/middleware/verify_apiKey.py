from fastapi import Request ,HTTPException
from dotenv import load_dotenv
import os
load_dotenv()

def verifyApiKey(request:Request):
    api_key=request.headers.get("X-API-KEY")
    if (not api_key or api_key !=os.getenv("API_KEY")):
        raise HTTPException(
            status_code=401,
            detail="invalid api key"
        )

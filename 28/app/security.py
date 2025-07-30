from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os

load_dotenv()

#name of API key header
API_KEY_NAME = "api-key"

#create an instance of APIKeyHeader
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

"""
An API key header is a specific type of HTTP request header used to 
transmit an API key from a client application to an API server
"""

def get_api_key(api_key: str = Depends(api_key_header)):
  allowed_api_keys = os.getenv("API_KEYS", "").split(",")
  
  print("Received API Key:", api_key)
  print("Allowed API Keys:", allowed_api_keys)

  if api_key not in allowed_api_keys:
    print("API Key not valid")
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Invalid API Key",
    )

  print("API Key valid")
  return api_key







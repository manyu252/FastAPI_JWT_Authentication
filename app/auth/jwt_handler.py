# This file is responsible for signing, encoding, decoding and returning JWT tokens

import time
import jwt
from decouple import config

JWT_SECRET = config('secret')
JWT_ALGORITHM = config('algorithm')

# Function to return generated tokens
def token_response(token: str):
    return {
        "access_token": token
    }

# Function to sign JWT string
def signJWT(user_id: str) -> dict:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

# Function to decode JWT string
def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
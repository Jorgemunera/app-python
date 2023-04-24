from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token, secret

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credenciales = await super().__call__(request)
        payload = validate_token(credenciales.credentials, secret)
        if payload['email'] != 'jorge@mail.com':
            raise HTTPException(status_code = 403, detail = 'credenciales son invalidas')
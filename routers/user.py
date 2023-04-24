from fastapi import APIRouter
from utils.jwt_manager import create_token, secret
from fastapi.responses import JSONResponse
from schemas.user import User

user_router = APIRouter()

@user_router.post('/login', tags = ['auth'], response_model = dict)
def login(user: User) -> dict:
    if user.email == 'jorge@mail.com' and user.password == 'jorge123':
        token:str = create_token(user.dict(), secret)
    return JSONResponse(status_code = 200,content = {
        'data': dict(user),
        'token': token
    })
from jwt import encode, decode

secret = 'my_secret'

def create_token(data: dict, secret):
    token: str = encode(payload = data, key = secret, algorithm = 'HS256')
    return token

def validate_token(token: str, secret) -> dict:
    payload:str = decode(token, key = secret, algorithms = ['HS256'])
    return payload
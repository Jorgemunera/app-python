from pydantic import BaseModel, Field

class User(BaseModel):
    email: str
    password: str = Field(min_length = 5,  max_length = 20)

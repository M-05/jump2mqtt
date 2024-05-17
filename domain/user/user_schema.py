from pydantic import BaseModel, constr, validator
import datetime

class UserCreate(BaseModel):
    username: constr(strip_whitespace=True, min_length=1, max_length=50) = 'test'
    create_date: datetime.datetime

    @validator('username')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용하지 않습니다.")
        return v        

class User(BaseModel):
    no: int
    username: str
    create_date: datetime.datetime

    class Config:
        from_attributes = True
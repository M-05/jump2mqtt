from pydantic import BaseModel, constr, validator, field_validator
import datetime

from domain.user import user_schema

class message(BaseModel):
    no: int
    username: str
    message: str
    create_date: datetime.datetime
    class Config:
        from_attributes = True


class messageCreate(BaseModel):
    message: str

    @field_validator('message')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용하지 않습니다.")
        return v
    
class messageList(BaseModel):
    message_list : list[message] = []
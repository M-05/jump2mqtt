from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.message import message_crud, message_schema
from domain.user import user_crud
import models

router = APIRouter(
    prefix="/message", tags=["message"]
)

@router.get('/list', response_model=message_schema.messageList)
def message_list(db: Session = Depends(get_db)):
    messages = message_crud.get_message_list(db=db)
    return {"msg_list" : [message_schema.message.from_orm(msg) for msg in messages]}

@router.get('/detail/{username}', response_model=message_schema.message)
def message_detail(db: Session= Depends(get_db), 
                    username: str = 'test'):
    return message_crud.get_message(db=db, user=username)

@router.post('/create', status_code=status.HTTP_204_NO_CONTENT)
async def message_create(message_create: message_schema.messageCreate,
                    username: str = 'test',
                    db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    message_crud.create_message(db=db, message_create=message_create, user=user)
    return Response(status_code=204)

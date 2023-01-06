from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session 
from blog import hashing
from .. import schemas, database, models
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=['users']
)

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)
    
    
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    return user.show(id, db)
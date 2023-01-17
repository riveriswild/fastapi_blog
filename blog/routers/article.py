from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from blog import oauth2

from .. import schemas, database, models
from sqlalchemy.orm import Session 
from ..repository import article

router = APIRouter(
    prefix='/article',
    tags=['articles']
)

get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowArticle])
def all(db: Session = Depends(database.get_db)):
    return article.get_all_articles(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.CreateArticle, db: Session = Depends(database.get_db)):
    return article.create_article(request, db)


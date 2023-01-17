from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .. import models

def get_all_articles(db:Session):
    articles = db.query(models.Article).all()
    return articles

def create_article(request, db:Session):
    new_article = models.Article(title=request.title, body=request.body, user_id=1, blog_id=1)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
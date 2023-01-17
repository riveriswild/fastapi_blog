# from http.client import HTTPException
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .. import models




def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get_all_articles(db:Session):
    articles = db.query(models.Article).all()
    return articles

def create(request, db:Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def create_article(request, db:Session):
    new_article = models.Article(title=request.title, body=request.body, user_id=1, blog_id=1)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

def destroy(id:int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int, request, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
    blog.update(request)
    db.commit()
    return 'done'

def show(id: int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} Not Found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details': f'blog with id {id} Not Found'}
    return blog
from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str

    
class Blog(BlogBase):
    class Config():
        orm_mode = True
        

class User(BaseModel):
    name: str
    email: str
    password: str

class ViewArticle(BaseModel):
    id: int
    title: str
    body: str
    class Config():
        orm_mode = True  
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    articles: List[ViewArticle] = []
    class Config():
        orm_mode = True

class SimpleUser(BaseModel):
    id: int
    name: str
    class Config():
        orm_mode = True
        
class Article(BaseModel):
    id: int
    title: str
    body: str
    author: SimpleUser
    class Config():
        orm_mode = True
class CreateArticle(BaseModel):
    id: int
    title: str
    body: str
    class Config():
        orm_mode = True

class ShowArticle(Article):
    title: str
    body: str
    
        
class ShowBlog(Blog):
    creator: ShowUser
    articles: List[Article] = []
    class Config():
        orm_mode = True
        

class Login(BaseModel):
    username: str
    password: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str
    

class TokenData(BaseModel):
    username: Optional[str] = None
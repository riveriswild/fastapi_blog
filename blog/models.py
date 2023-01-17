from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.orm import relationship

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    blog_id = Column(Integer, ForeignKey('blogs.id'))
    blog = relationship("Blog", back_populates='articles')
    author = relationship("User", back_populates='articles')
    
class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    articles = relationship("Article", back_populates='blog')
    
    creator = relationship("User", back_populates='blogs')
    

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    blogs = relationship("Blog", back_populates='creator')
    articles = relationship("Article", back_populates='author')
    

    
# class Comment(Base):
#     __tablename__ = 'comments'
#     id = Column(Integer, primary_key=True, index=True)
#     body = Column(String)
#     user_id = Column(Integer, ForeignKey('users.id'))
    
#     creator = relationship("User", back_populates='comments')
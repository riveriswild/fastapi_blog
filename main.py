from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()

@app.get('/')
def index():
    return ""


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title {blog.title}'}


# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port=9000)
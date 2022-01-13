from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from psycopg2.extras import RealDictCursor
import psycopg2
import time

from app.utils import delete_post, find_index, find_post, hardcoded_posts

app = FastAPI()


class Post(BaseModel):
    title: str
    body: str
    published: bool = True
    rating: Optional[int] = None


while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='myfastapi_db',
            user='postgres',
            password='gmG~8UPW',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print('Database connection was successful.')
        break
    except Exception as e:
        print('Connection failed')
        print('Errors: ', e)
        time.sleep(2)


@app.get('/')
async def root():
    return {'message': "Hello world"}


@app.get('/posts')
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {'data': posts}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute("""INSERT INTO posts (title, body, published) VALUES (%s, %s, %s) RETURNING *""",
                   (post.title, post.body, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {'data': new_post}


# @app.get('/posts/latest')
# def get_latest_post():
#     cursor.execute("""SELECT * FROM posts WHERE id = %s""", ())
#     post = cursor.fetchone()
#     return {"post_detail": post}


@app.get('/posts/{id}')
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found.')
    return {"post_detail": post}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(
        """DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found.')
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title=%s, body=%s, published=%s WHERE id=%s RETURNING *""",
                   (post.title, post.body, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'post with id: {id} was not found.')
    return {'post': updated_post}

from fastapi import FastAPI
from models import User

app = FastAPI()

posts={}

@app.get("/home")
async def check_posts():
    return posts

@app.post("/post")
async def create_post(title:str, contents:str, user:User):
    post_id = user.id
    posts[post_id] = {"title":title, "contents":contents, "user_name":user.name}
    return posts[post_id]
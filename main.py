import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema, UserSchema, LoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer

posts = [
    {
        "id": 1,
        "title": "Demo Post 1",
        "content": "Demo Content 1"
    },
    {
        "id": 2,
        "title": "Demo Post 2",
        "content": "Demo Content 2"
    }
]

users = []

app = FastAPI()

@app.get("/", tags=["test"])
def greet():
    return {"Hello": "World"}

@app.get("/posts", tags=["posts"])
def get_posts():
    return posts

@app.get("/posts/{post_id}", tags=["posts"])
def get_one_post(post_id: int):
    if post_id > len(posts):
        return {"Error": "Post ID does not exist"}
    return {
        "data": posts[post_id-1]
    }

@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
def create_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "info": "Post added"
    }

# User signup 
@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user.dict())
    return signJWT(user.email)

# check user
def check_user(data: LoginSchema):
    for user in users:
        if user["email"] == data.email and user["password"] == data.password:
            return True
    return False

# User login
@app.post("/user/login", tags=["user"])
def user_login(user: LoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    return {"Error": "Invalid credentials"}
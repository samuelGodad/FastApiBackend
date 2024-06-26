from fastapi import FastAPI
from app.routers import user, post

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

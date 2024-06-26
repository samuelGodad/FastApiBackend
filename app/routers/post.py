from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.post import PostCreate, PostResponse
from app.crud import post as crud_post
from app.utils.auth import verify_token, oauth2_scheme
from app.database import get_db
from cachetools import cached, TTLCache

router = APIRouter()

cache = TTLCache(maxsize=100, ttl=300)

@router.post("/posts", response_model=PostResponse)
def create_post(post: PostCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    token_data = verify_token(token, credentials_exception)
    user = crud_user.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return crud_post.create_post(db=db, post=post, user_id=user.id)

@router.get("/posts", response_model=list[PostResponse])
@cached(cache)
def get_posts(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    token_data = verify_token(token, credentials_exception)
    user = crud_user.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return crud_post.get_posts_by_user(db=db, user_id=user.id)

@router.delete("/posts/{post_id}", response_model=dict)
def delete_post(post_id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    token_data = verify_token(token, credentials_exception)
    user = crud_user.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    success = crud_post.delete_post(db=db, post_id=post_id, user_id=user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found or not authorized")
    return {"message": "Post deleted successfully"}

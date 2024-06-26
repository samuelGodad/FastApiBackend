from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate

def create_post(db: Session, post: PostCreate, user_id: int):
    db_post = Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts_by_user(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def delete_post(db: Session, post_id: int, user_id: int):
    db_post = db.query(Post).filter(Post.id == post_id, Post.user_id == user_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
        return True
    return False

from sqlalchemy.orm import Session
from api import models, schemas


def get_meme(db: Session, meme_id: int):
    return db.query(models.Meme).filter(
        models.Meme.id == meme_id
    ).first()


def get_memes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Meme).offset(skip).limit(limit).all()


def create_meme(db: Session, meme: schemas.MemeCreate):
    db_meme = models.Meme(
        title=meme.title,
        description=meme.description,
        image_url=meme.image_url
    )
    db.add(db_meme)
    db.commit()
    db.refresh(db_meme)
    return db_meme


def update_meme(db: Session, meme_id: int, meme: schemas.MemeUpdate):
    db_meme = db.query(models.Meme).filter(
        models.Meme.id == meme_id
    ).first()
    if meme.title:
        db_meme.title = meme.title
    if meme.description:
        db_meme.description = meme.description
    if meme.image_url:
        db_meme.image_url = meme.image_url
    db.commit()
    return db_meme


def delete_meme(db: Session, meme_id: int):
    db_meme = db.query(models.Meme).filter(
        models.Meme.id == meme_id
    ).first()
    db.delete(db_meme)
    db.commit()
    return db_meme

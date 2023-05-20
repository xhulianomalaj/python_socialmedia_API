from fastapi import FastAPI, HTTPException, Depends, APIRouter, status, Response
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/comments",
    tags=['Comments']
)

@router.get("/", response_model=List[schemas.CommentOut])
def get_comments(db: Session = Depends(get_db)):
    comments = db.query(models.Comment).all()
    return comments





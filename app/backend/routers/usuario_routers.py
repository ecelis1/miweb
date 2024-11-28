from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.services.usuario_services import create_user, get_user, get_user_by_email, update_user, delete_user
from backend.schemas.usuario_schemas import UserCreate, UserUpdate, UserOut
from backend.config.database import SessionLocal

router = APIRouter()

@router.post("/users/", response_model=UserOut)
def create_user_route(user: UserCreate, db: Session = Depends(SessionLocal)):
    return create_user(db, user)

@router.get("/users/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(SessionLocal)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/users/{user_id}", response_model=UserOut)
def update_user_route(user_id: int, user: UserUpdate, db: Session = Depends(SessionLocal)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user(db, user_id, user)

@router.delete("/users/{user_id}", response_model=UserOut)
def delete_user_route(user_id: int, db: Session = Depends(SessionLocal)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(db, user_id)
    return db_user


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.models.producto import CarritoItem
from backend.config.database import get_db
from backend.schemas.carrito_schemas import CarritoItemCreate

router = APIRouter()

@router.post("/carrito/",tags=['CARRITO'], response_model=CarritoItemCreate)
def add_to_carrito(item: CarritoItemCreate, db: Session = Depends(get_db)):
    carrito_item = CarritoItem(**item.dict())
    db.add(carrito_item)
    db.commit()
    db.refresh(carrito_item)
    return carrito_item

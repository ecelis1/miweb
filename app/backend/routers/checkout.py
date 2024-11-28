from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.producto import Carrito, Pedido
from app.config.database import get_db
from schemas import PedidoCreate

router = APIRouter()

@router.post("/checkout/", tags=['CARRITO'], response_model=PedidoCreate)
def checkout(pedido: PedidoCreate, db: Session = Depends(get_db)):
    # Consultar el carrito del usuario según el pedido recibido
    carrito = db.query(Carrito).filter(Carrito.user_id == pedido.user_id).first()
    # Si no se encuentra el carrito, devolver un error 404
    if not carrito:
        raise HTTPException(status_code=404, detail="Carrito no encontrado")
    # Calcular el total sumando el precio de cada producto en el carrito
    total = sum(item.product.price * item.quantity for item in carrito.items)
    # Crear un nuevo pedido con el user_id del pedido y el total calculado
    new_pedido = Pedido(user_id=pedido.user_id, total=total)
    # Agregar el nuevo pedido a la sesión de base de datos
    db.add(new_pedido)
    # Confirmar los cambios en la base de datos
    db.commit()
    # Actualizar el objeto new_pedido con cualquier cambio realizado en la base de datos
    db.refresh(new_pedido)
    # Devolver el nuevo pedido creado como respuesta
    return new_pedido


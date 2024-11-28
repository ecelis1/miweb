from pydantic import BaseModel

class CarritoItemCreate(BaseModel):
    carrito_id: int
    product_id: int
    quantity: int

class PedidoCreate(BaseModel):
    user_id: int

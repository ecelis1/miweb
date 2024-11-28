from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from backend.config.database import Base
from ..models.carrito_models import CarritoItem

#CARRITO
class Carrito(Base):
    __tablename__ = "carritos"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("usuarios.id"))
    items = relationship("CarritoItem", back_populates="carrito")

#ITEMS CARRITO
class CarritoItem(Base):
    __tablename__ = "carrito_items"
    id = Column(Integer, primary_key=True, index=True)
    carrito_id = Column(Integer, ForeignKey("carritos.id"))
    product_id = Column(Integer, ForeignKey("productos.id"))
    quantity = Column(Integer)
    carrito = relationship("Carrito", back_populates="items")
    product = relationship("Producto", back_populates="carrito_items")
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from backend.config.database import Base


#PRODUCTO
class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), index=True)
    description = Column(String(30))
    price = Column(Float)
    stock = Column(Integer)



#PEDIDOS
class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("usuarios.id"))
    total = Column(Float)
    status = Column(String(30), default="Pendiente")


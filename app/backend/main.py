from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from routers import carrito, checkout, usuario_routers
from backend.config.database import engine, Base, SessionLocal
from starlette.middleware.cors import CORSMiddleware
from backend.models.carrito_models import CarritoItem
import mercadopago



app = FastAPI()

origins = [
    "http://127.0.0.1:5501",  # Origen de tu HTML
    "http://localhost:5501",  # Origen de tu HTML (alternativo)
    "http://127.0.0.1:5500",  # Origen de tu HTML
    "http://localhost:5500",  # Origen de tu HTML (alternativo)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(carrito.router)
app.include_router(checkout.router)
app.include_router(usuario_routers.router)



# Configurar la clave de acceso de MercadoPago
sdk = mercadopago.SDK("tu_access_token_de_mercadopago")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


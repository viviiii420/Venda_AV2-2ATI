# app.py
# FastAPI app para o sistema de vendas
from fastapi import FastAPI, HTTPException
from database import get_db, create_tables
from models import Venda

app = FastAPI()

@app.on_event("startup")
def startup():
    create_tables()

@app.get("/vendas", response_model=list[Venda])
def listar_vendas():
    db = get_db()
    vendas = db.query(Venda).all()
    return vendas

# ...rotas RESTful (200, 201, 400, 404, 422, 500)

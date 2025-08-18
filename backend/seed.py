# seed.py
from database import SessionLocal, create_tables
from models import Venda

def seed():
    create_tables()
    db = SessionLocal()
    vendas = [
        Venda(produto="Produto A", quantidade=2, preco=19.99),
        Venda(produto="Produto B", quantidade=5, preco=9.99),
        Venda(produto="Produto C", quantidade=1, preco=99.99),
        Venda(produto="Produto D", quantidade=3, preco=29.99),
        Venda(produto="Produto E", quantidade=4, preco=49.99),
        Venda(produto="Produto F", quantidade=2, preco=15.99),
        Venda(produto="Produto G", quantidade=6, preco=5.99),
        Venda(produto="Produto H", quantidade=1, preco=199.99),
        Venda(produto="Produto I", quantidade=7, preco=3.99),
        Venda(produto="Produto J", quantidade=2, preco=39.99),
        Venda(produto="Produto K", quantidade=1, preco=59.99),
        Venda(produto="Produto L", quantidade=8, preco=2.99),
        Venda(produto="Produto M", quantidade=3, preco=24.99),
        Venda(produto="Produto N", quantidade=2, preco=44.99),
        Venda(produto="Produto O", quantidade=5, preco=12.99),
        Venda(produto="Produto P", quantidade=1, preco=149.99),
        Venda(produto="Produto Q", quantidade=4, preco=34.99),
        Venda(produto="Produto R", quantidade=2, preco=27.99),
        Venda(produto="Produto S", quantidade=6, preco=7.99),
        Venda(produto="Produto T", quantidade=1, preco=89.99),
    ]
    db.add_all(vendas)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed()

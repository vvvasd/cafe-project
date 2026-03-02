from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

menu = [
    {"id": 1, "name": "Бургер", "price": 250},
    {"id": 2, "name": "Картошка", "price": 120},
    {"id": 3, "name": "Кола", "price": 100}
]

orders = []

@app.get("/menu")
def get_menu():
    return menu

@app.post("/order")
def create_order(order: dict):
    orders.append(order)
    return {"status": "заказ принят", "order": order}

@app.get("/")
def root():
    return {"message": "Cafe backend works"}

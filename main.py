from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

# List of available fruits
items_list: List[Item] = [
    Item(id=1, name="Orange", price=25.0, quantity=5),
    Item(id=2, name="Apple", price=30.0, quantity=10),
    Item(id=3, name="Banana", price=15.0, quantity=20),
    Item(id=4, name="Mango", price=50.0, quantity=8),
    Item(id=5, name="Grapes", price=40.0, quantity=12),
]

# Shopping cart storage
shopping_cart_items: List[Item] = []

@app.get("/cart/", response_model=List[Item])
def get_cart_items():
    return shopping_cart_items

@app.get("/items/", response_model=List[Item])
def get_fruits():
    return items_list

@app.post("/additem/")
def add_item(item: Item):
    items_list.append(item)
    return {"message": "Item added successfully", "item": item}

@app.post("/order/")
def add_item(item: Item):
    shopping_cart_items.append(item)
    return {"message": "Item added to cart successfully", "item": item}

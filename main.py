from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model
class Item(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

# Create a list to hold items
itemsList = [
    {"id": 1, "name": "Orange", "price": 25.0, "quantity": 5},
    {"id": 2, "name": "Apple", "price": 30.0, "quantity": 10},
    {"id": 3, "name": "Banana", "price": 15.0, "quantity": 20},
    {"id": 4, "name": "Mango", "price": 50.0, "quantity": 8},
    {"id": 5, "name": "Grapes", "price": 40.0, "quantity": 12},
]

#Holds the items
ShoppingCartItems = []

# Endpoint to get the items from the cart
@app.get("/cart/")
def read_items():
 return {"Shopping Cart": ShoppingCartItems}

# Endpoint to the get items
@app.get("/fruits/")
def read_items():
    return {"Fruits": itemsList}

# Endpoint to add items
@app.post("/items/")
def add_item(item: Item):
    ShoppingCartItems.append(item)  # Convert Pydantic model to dict
    return {"message": "Item added successfully", "item": item}

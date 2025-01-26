from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model
class Item(BaseModel):
    name: str
    amount: int

# Create a list to hold items
items = []

@app.get("/items/")
def read_items():
    return {"message": "orange"}

# If you want to add an endpoint to add items
@app.post("/items/")
def add_item(item: Item):
    items.append(item)
    return {"message": "Item added successfully", "item": item}

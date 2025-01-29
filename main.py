from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model
class Item(BaseModel):
    name: str


# Create a list to hold items

itemsList = {"orange", "banana", "watermelon", "strawberry"}
items = []

@app.get("/fruits/")
def read_items():
    return {"Fruits": itemsList}

# If you want to add an endpoint to add items
@app.post("/items/")
def add_item(item: Item):
    items.append(item)
    return {"message": "Item added successfully", "item": item}

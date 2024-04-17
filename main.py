from fastapi import FastAPI

from models import Item

import json

app = FastAPI()

with open("store_items.json", "r") as f:
    json_data = json.load(f)

@app.get("/items")
async def get_items() -> list:
    return json_data

@app.post("/items")
async def create_item(item: Item):
    json_data.append(item.model_dump())
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    json_data[item_id-1] = item.model_dump()
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    deleted_item = json_data.pop(item_id-1)
    return deleted_item
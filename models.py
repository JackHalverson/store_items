from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int

class ItemCreate(BaseModel):
    name: str
    description: str
    price: int

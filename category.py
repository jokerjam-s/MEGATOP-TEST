from typing import List, Optional

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    parent: int | None = None
    name: str
    url: str
    level: int = 0
    query: str | None = None
    shard: str | None = None
    childs: list['Category'] | None = None


class Colors(BaseModel):
    id: int
    name: str

class Price(BaseModel):
    basic: int
    product: int
    total: int
    logistics: int


class Size(BaseModel):
    id: int
    name: str
    origName: str
    price: Price | None = None,
    saleConditions: int


class Goods(BaseModel):
    id: int
    dist: int
    brand: str | None = None
    colors: list[Colors] | None = None
    name: str
    supplier: str
    supplierId: int
    supplierRating: float
    rating: int
    reviewRating: float
    feedbacks: int
    volume: int
    sizes: list[Size] | None = None
    totalQuantity: int
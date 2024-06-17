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

    def __str__(self):
        return f'{self.id}-{self.name}'


class Colors(BaseModel):
    id: int
    name: str

    def __str__(self):
        return self.name


class Size(BaseModel):
    name: str
    origName: str

    def __str__(self):
        return self.name


class Product(BaseModel):
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
    volume: int
    sizes: list[Size] | None = None
    priceU: int
    totalQuantity: int


class ProductsInfo(BaseModel):
    categories_full_path: str | None = None
    prods_list: list[Product] = list()

from decimal import Decimal

from pydantic import BaseModel

from app.models.categories import Category


class Product(BaseModel):
    name: str
    price: Decimal
    category: Category

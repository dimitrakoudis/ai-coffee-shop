from decimal import Decimal

from pydantic import BaseModel

from app.models.categories import Category


class Product(BaseModel):
    name: str
    price: Decimal
    category: Category

    @property
    def is_drink(self) -> bool:
        return self.category in (
            Category.SOFT_DRINK,
            Category.TEA,
            Category.COFFEE,
        )

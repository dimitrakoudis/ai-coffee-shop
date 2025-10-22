from pydantic import BaseModel

from app.models.product import Product


class Menu(BaseModel):
    products: list[Product]

    @property
    def products_map(self) -> dict[str, Product]:
        return {product.name: product for product in self.products}

    def get_product_by_name(self, name: str) -> Product | None:
        return self.products_map.get(name)

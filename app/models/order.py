import uuid
from decimal import Decimal

from app.models.product import Product


class Order:
    def __init__(
        self,
        order_id: str | None = None,
        products: list[Product] | None = None,
    ) -> None:
        self._order_id = order_id or str(uuid.uuid4())
        self._products = products or []

    @property
    def order_id(self) -> str:
        return self._order_id

    def add_product(self, product: Product) -> None:
        self._products.append(product)

    @property
    def total(self) -> Decimal:
        return Decimal(str(sum([product.price for product in self._products])))

from pydantic import BaseModel

from app.models.categories import Category


class WhenToUpsell(BaseModel):
    category_ordered: list[Category]


class Upsell(BaseModel):
    name: str
    try_per_order: int
    item_to_upsell: str
    when: WhenToUpsell

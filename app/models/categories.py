from enum import Enum


class Category(str, Enum):
    COFFEE = "coffee"
    TEA = "tea"
    SOFT_DRINK = "soft drink"
    BASIC = "basic"
    SIDE = "side"

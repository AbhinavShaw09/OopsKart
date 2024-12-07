from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name.replace("_", "").title()) for choice in cls]
    
    @classmethod
    def values(cls):
        return [tag.value for tag in cls]


class ProductCategoryChoices(BaseEnum):
    SPORTS = 1
    ELECTRONICS = 2
    HARDWARE = 3
    KITCHEN_AND_DINING = 4
    FURNITURE = 5
    HOME_DECOR = 6
    LIGHTING = 7


class GenderChoices(BaseEnum):
    MALE = 1
    FEMALE = 2
    OTHERS = 3


class CountryChoices(BaseEnum):
    India = 1
    USA = 2
    UK = 3
    Canada = 4
    Australia = 5
    Germany = 6
    France = 7
    Italy = 8
    Japan = 9
    China = 10
    Brazil = 11
    South_Africa = 12
    Russia = 13
    Mexico = 14
    South_Korea = 15


class ProductSizeChoices(BaseEnum):
    xs = 1
    sm = 2
    md = 3
    lg = 4
    xl = 5
    xxl = 6

from enum import Enum
from .attack import Attack
from .defense import Defense, Modifier

class Tag(Enum):
    powerful = 1
    precise = 2
    quick = 3

class Type(Enum):
    strike = 1
    grapple = 2
    throw = 3


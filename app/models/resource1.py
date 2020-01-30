from enum import Enum
from typing import List

from pydantic import BaseModel


class ExampleEnum(Enum):
    VALUE1 = 'VALUE1'
    VALUE2 = 'VALUE2'
    VALUE3 = 'VALUE3'


class Resource1(BaseModel):
    id: int
    stringfield: str
    enumfield: ExampleEnum
    listfield: List[str]

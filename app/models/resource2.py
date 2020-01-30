from typing import List

from pydantic import BaseModel

from app.models import Resource1


class Resource2(BaseModel):
    id: int
    children: List[Resource1]

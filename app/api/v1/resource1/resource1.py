from typing import List

from fastapi import APIRouter

from app.models import Resource1

router = APIRouter()


@router.get('/', response_model=List[Resource1])
def list_resource1s():
    return []


@router.post('/', response_model=Resource1)
def create_resource1(new_resource: Resource1):
    # Add to db, etc.
    return new_resource

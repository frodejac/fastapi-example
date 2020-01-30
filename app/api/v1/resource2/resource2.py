from typing import List

from fastapi import APIRouter, HTTPException

from app.models import Resource2

router = APIRouter()


@router.get('/', response_model=List[Resource2])
def list_resource2s():
    return []


@router.post('/', response_model=Resource2)
def create_resource2(new_resource: Resource2):
    # Add to db, etc.
    return new_resource


@router.get('/{resource_id}/', response_model=Resource2)
def get_resource_by_id(resource_id: int):
    raise HTTPException(404, f'resource with id {resource_id} not found')

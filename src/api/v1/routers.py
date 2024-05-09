from fastapi import APIRouter

from api.v1.endpoints import films_router, persons_router

main_router = APIRouter()

main_router.include_router(
    films_router,
    prefix='/films',
    tags=['Films'],
)

main_router.include_router(
    persons_router,
    prefix='/persons',
    tags=['Persons'],
)
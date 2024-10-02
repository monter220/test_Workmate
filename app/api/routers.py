from fastapi import APIRouter

from app.api.endpoints import kitty_router, colour_router, breed_router
from app.core.config import settings


main_router = APIRouter(prefix=f'/api/v{str(settings.api_version)}')
main_router.include_router(kitty_router)
main_router.include_router(colour_router)
main_router.include_router(breed_router)

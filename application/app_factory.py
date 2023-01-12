from fastapi import APIRouter, FastAPI

from apps.async_app import router as async_router
from apps.sync_app import router as sync_router


def create_app() -> FastAPI:
    routers: tuple[APIRouter, APIRouter] = (
        async_router,
        sync_router,
    )
    app: "FastAPI" = FastAPI()
    router: "APIRouter" = APIRouter(prefix="/api")
    [router.include_router(app_router) for app_router in routers]
    app.include_router(router)
    return app

from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import user_router
app = FastAPI(title="User Service")

app.include_router(user_router.router)
# app = FastAPI(title=settings.app_name, version=settings.app_version)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": settings.app_version,
        "env": settings.app_env,
    }

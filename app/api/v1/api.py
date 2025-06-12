from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, nutrition, recipes, activities

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(nutrition.router, prefix="/nutrition", tags=["nutrition"])
api_router.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
api_router.include_router(activities.router, prefix="/activities", tags=["activities"])
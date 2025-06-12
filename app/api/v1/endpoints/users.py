from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_current_active_user
from app.models.user import User
from app.schemas.user import User as UserSchema, UserUpdate, UserGoals
from app.crud.user import update_user
from app.db.database import get_db

router = APIRouter()

@router.get("/me", response_model=UserSchema)
async def get_current_user(current_user: User = Depends(get_current_active_user)):
    """Get current user profile."""
    return current_user

@router.put("/me", response_model=UserSchema)
async def update_current_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Update current user profile."""
    updated_user = update_user(db, user_id=current_user.id, user_update=user_update)
    return updated_user

@router.post("/goals", response_model=UserSchema)
async def set_user_goals(
    goals: UserGoals,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Set user's daily macro goals."""
    # Convert UserGoals to UserUpdate format for the update function
    goals_update = UserUpdate(
        daily_calories_target=goals.daily_calories_target,
        daily_protein_target=goals.daily_protein_target,
        daily_carbs_target=goals.daily_carbs_target,
        daily_fat_target=goals.daily_fat_target
    )
    updated_user = update_user(db, user_id=current_user.id, user_update=goals_update)
    return updated_user
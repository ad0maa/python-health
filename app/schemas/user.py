from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from app.models.user import ActivityLevel, Goal

class UserBase(BaseModel):
    email: EmailStr
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    gender: Optional[str] = None
    activity_level: Optional[ActivityLevel] = ActivityLevel.MODERATELY_ACTIVE
    primary_goal: Optional[Goal] = Goal.MAINTAIN_WEIGHT
    target_weight_kg: Optional[float] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    gender: Optional[str] = None
    activity_level: Optional[ActivityLevel] = None
    primary_goal: Optional[Goal] = None
    target_weight_kg: Optional[float] = None
    dietary_restrictions: Optional[str] = None
    allergies: Optional[str] = None
    preferred_cuisines: Optional[str] = None

class UserGoals(BaseModel):
    daily_calories_target: Optional[int] = None
    daily_protein_target: Optional[float] = None
    daily_carbs_target: Optional[float] = None
    daily_fat_target: Optional[float] = None

class User(UserBase):
    id: int
    is_active: bool
    daily_calories_target: Optional[int] = None
    daily_protein_target: Optional[float] = None
    daily_carbs_target: Optional[float] = None
    daily_fat_target: Optional[float] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
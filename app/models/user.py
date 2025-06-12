from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base
import enum

class ActivityLevel(str, enum.Enum):
    SEDENTARY = "sedentary"
    LIGHTLY_ACTIVE = "lightly_active"
    MODERATELY_ACTIVE = "moderately_active"
    VERY_ACTIVE = "very_active"
    EXTRA_ACTIVE = "extra_active"

class Goal(str, enum.Enum):
    MAINTAIN_WEIGHT = "maintain_weight"
    LOSE_WEIGHT = "lose_weight"
    GAIN_WEIGHT = "gain_weight"
    BUILD_MUSCLE = "build_muscle"
    IMPROVE_FITNESS = "improve_fitness"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    # Profile information
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    height_cm = Column(Float)
    weight_kg = Column(Float)
    gender = Column(String)  # male, female, other
    
    # Health goals and preferences
    activity_level = Column(Enum(ActivityLevel), default=ActivityLevel.MODERATELY_ACTIVE)
    primary_goal = Column(Enum(Goal), default=Goal.MAINTAIN_WEIGHT)
    target_weight_kg = Column(Float)
    
    # Daily macro targets (calculated based on goals)
    daily_calories_target = Column(Integer)
    daily_protein_target = Column(Float)
    daily_carbs_target = Column(Float)
    daily_fat_target = Column(Float)
    
    # Dietary restrictions and preferences
    dietary_restrictions = Column(Text)  # JSON string of restrictions
    allergies = Column(Text)  # JSON string of allergies
    preferred_cuisines = Column(Text)  # JSON string of preferred cuisines
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships (will add back when other models are ready)
    # meals = relationship("Meal", back_populates="user")
    # recipes = relationship("Recipe", back_populates="user")
    # activities = relationship("Activity", back_populates="user")
    # user_integrations = relationship("UserIntegration", back_populates="user")
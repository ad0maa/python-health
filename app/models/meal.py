from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Meal information
    meal_type = Column(String)  # breakfast, lunch, dinner, snack
    meal_name = Column(String)  # optional custom name
    consumed_at = Column(DateTime(timezone=True), default=func.now())
    
    # Calculated totals (computed from meal_foods)
    total_calories = Column(Float, default=0)
    total_protein = Column(Float, default=0)
    total_carbs = Column(Float, default=0)
    total_fat = Column(Float, default=0)
    total_fiber = Column(Float, default=0)
    
    # Optional notes
    notes = Column(Text)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="meals")
    meal_foods = relationship("MealFood", back_populates="meal", cascade="all, delete-orphan")

class MealFood(Base):
    __tablename__ = "meal_foods"

    id = Column(Integer, primary_key=True, index=True)
    meal_id = Column(Integer, ForeignKey("meals.id"))
    food_id = Column(Integer, ForeignKey("foods.id"))
    
    # Serving information
    quantity = Column(Float)  # Amount consumed
    unit = Column(String)  # grams, cups, pieces, etc.
    weight_grams = Column(Float)  # Actual weight in grams for calculation
    
    # Calculated nutrition for this serving
    calories = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fat = Column(Float)
    fiber = Column(Float)
    
    # Relationships
    meal = relationship("Meal", back_populates="meal_foods")
    food = relationship("Food", back_populates="meal_foods")
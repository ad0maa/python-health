from sqlalchemy import Column, Integer, String, Float, Text, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand = Column(String)
    
    # Nutritional information per 100g
    calories_per_100g = Column(Float)
    protein_per_100g = Column(Float)
    carbs_per_100g = Column(Float)
    fat_per_100g = Column(Float)
    fiber_per_100g = Column(Float)
    sugar_per_100g = Column(Float)
    sodium_per_100g = Column(Float)  # mg
    
    # Additional nutrients
    vitamin_c_per_100g = Column(Float)  # mg
    iron_per_100g = Column(Float)  # mg
    calcium_per_100g = Column(Float)  # mg
    
    # Food categorization
    category = Column(String)  # fruits, vegetables, grains, proteins, etc.
    subcategory = Column(String)
    
    # External API references
    usda_fdc_id = Column(String)  # USDA FoodData Central ID
    spoonacular_id = Column(String)  # Spoonacular API ID
    
    # Serving information
    common_serving_size = Column(String)  # "1 cup", "1 slice", etc.
    common_serving_weight_g = Column(Float)
    
    # Metadata
    description = Column(Text)
    is_verified = Column(Boolean, default=False)  # Admin verified food
    
    # Relationships
    meal_foods = relationship("MealFood", back_populates="food")
    recipe_ingredients = relationship("RecipeIngredient", back_populates="food")
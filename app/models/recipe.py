from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Recipe information
    name = Column(String, index=True)
    description = Column(Text)
    instructions = Column(Text)
    prep_time_minutes = Column(Integer)
    cook_time_minutes = Column(Integer)
    servings = Column(Integer)
    
    # Recipe categorization
    cuisine_type = Column(String)  # italian, mexican, asian, etc.
    meal_type = Column(String)  # breakfast, lunch, dinner, snack, dessert
    difficulty_level = Column(String)  # easy, medium, hard
    
    # Nutritional information (per serving)
    calories_per_serving = Column(Float)
    protein_per_serving = Column(Float)
    carbs_per_serving = Column(Float)
    fat_per_serving = Column(Float)
    fiber_per_serving = Column(Float)
    
    # Recipe metadata
    is_public = Column(Boolean, default=False)  # Can other users see this recipe?
    is_favorite = Column(Boolean, default=False)  # User favorite
    image_url = Column(String)  # Recipe photo
    source_url = Column(String)  # Original source if imported
    
    # External API references
    spoonacular_id = Column(String)
    
    # Recipe tags (for filtering and recommendations)
    tags = Column(Text)  # JSON string: ["vegetarian", "gluten-free", "high-protein"]
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="recipes")
    ingredients = relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan")

class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    food_id = Column(Integer, ForeignKey("foods.id"))
    
    # Ingredient information
    quantity = Column(Float)
    unit = Column(String)  # cups, tbsp, grams, etc.
    weight_grams = Column(Float)  # Converted to grams for calculations
    
    # Optional ingredient notes
    preparation = Column(String)  # "diced", "chopped", "cooked", etc.
    is_optional = Column(Boolean, default=False)
    
    # Calculated nutrition contribution
    calories = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fat = Column(Float)
    
    # Relationships
    recipe = relationship("Recipe", back_populates="ingredients")
    food = relationship("Food", back_populates="recipe_ingredients")
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Activity information
    activity_type = Column(String)  # running, cycling, weightlifting, etc.
    name = Column(String)  # Custom activity name
    description = Column(Text)
    
    # Time and duration
    started_at = Column(DateTime(timezone=True))
    ended_at = Column(DateTime(timezone=True))
    duration_minutes = Column(Integer)
    
    # Activity metrics
    distance_km = Column(Float)  # For cardio activities
    calories_burned = Column(Float)
    avg_heart_rate = Column(Integer)  # BPM
    max_heart_rate = Column(Integer)  # BPM
    
    # Cardio specific metrics
    avg_pace_min_per_km = Column(Float)  # For running/cycling
    elevation_gain_m = Column(Float)
    
    # Strength training metrics
    sets = Column(Integer)
    reps = Column(Integer)
    weight_kg = Column(Float)
    
    # Data source
    source = Column(String)  # manual, strava, apple_health, fitbit, etc.
    external_id = Column(String)  # ID from external service
    
    # Sync information
    last_synced_at = Column(DateTime(timezone=True))
    sync_status = Column(String, default="synced")  # synced, pending, failed
    
    # Metadata
    notes = Column(Text)
    is_public = Column(Boolean, default=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="activities")

class UserIntegration(Base):
    __tablename__ = "user_integrations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Integration information
    service_name = Column(String)  # strava, apple_health, fitbit, etc.
    is_active = Column(Boolean, default=True)
    
    # OAuth tokens (encrypted)
    access_token = Column(Text)  # Encrypted
    refresh_token = Column(Text)  # Encrypted
    token_expires_at = Column(DateTime(timezone=True))
    
    # Sync preferences
    auto_sync_enabled = Column(Boolean, default=True)
    sync_activities = Column(Boolean, default=True)
    sync_heart_rate = Column(Boolean, default=True)
    sync_weight = Column(Boolean, default=True)
    
    # Last sync information
    last_sync_at = Column(DateTime(timezone=True))
    last_sync_status = Column(String)  # success, failed, partial
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="user_integrations")
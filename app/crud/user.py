from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password
from typing import Optional


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Get user by email address."""
    stmt = select(User).where(User.email == email)
    return db.scalar(stmt)


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    """Get user by ID."""
    stmt = select(User).where(User.id == user_id)
    return db.scalar(stmt)


def create_user(db: Session, user: UserCreate) -> User:
    """Create a new user."""
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age,
        height_cm=user.height_cm,
        weight_kg=user.weight_kg,
        gender=user.gender,
        activity_level=user.activity_level,
        primary_goal=user.primary_goal,
        target_weight_kg=user.target_weight_kg,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
    """Update user information."""
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None

    update_data = user_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    """Authenticate user with email and password."""
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

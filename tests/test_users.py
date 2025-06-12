import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.models.user import User, ActivityLevel, Goal
from app.schemas.user import UserCreate, UserUpdate, UserGoals
from app.crud.user import create_user, get_user_by_email
from app.core.security import create_access_token


class TestUserEndpoints:
    """Test suite for user management endpoints."""

    def test_get_current_user_authenticated(self, client: TestClient, test_db: Session, test_user: User):
        """Test getting current user profile with valid authentication."""
        # Create access token for test user
        access_token = create_access_token(data={"sub": test_user.email})
        headers = {"Authorization": f"Bearer {access_token}"}

        response = client.get("/api/v1/users/me", headers=headers)
        assert response.status_code == 200

        data = response.json()
        assert data["email"] == test_user.email
        assert data["username"] == test_user.username
        assert data["id"] == test_user.id
        assert data["is_active"] == test_user.is_active

    def test_get_current_user_unauthenticated(self, client: TestClient):
        """Test getting current user profile without authentication."""
        response = client.get("/api/v1/users/me")
        assert response.status_code == 403

    def test_get_current_user_invalid_token(self, client: TestClient):
        """Test getting current user profile with invalid token."""
        headers = {"Authorization": "Bearer invalid_token"}
        response = client.get("/api/v1/users/me", headers=headers)
        assert response.status_code == 401

    def test_update_current_user_success(self, client: TestClient, test_db: Session, test_user: User):
        """Test updating current user profile successfully."""
        access_token = create_access_token(data={"sub": test_user.email})
        headers = {"Authorization": f"Bearer {access_token}"}

        update_data = {
            "first_name": "Updated",
            "last_name": "User",
            "age": 30,
            "height_cm": 175.5,
            "weight_kg": 70.0,
            "gender": "male",
            "activity_level": "very_active",
            "target_weight_kg": 65.0
        }

        response = client.put("/api/v1/users/me",
                              json=update_data, headers=headers)
        assert response.status_code == 200

        data = response.json()
        assert data["first_name"] == "Updated"
        assert data["last_name"] == "User"
        assert data["age"] == 30
        assert data["height_cm"] == 175.5
        assert data["weight_kg"] == 70.0
        assert data["gender"] == "male"
        assert data["activity_level"] == "very_active"
        assert data["target_weight_kg"] == 65.0

    def test_update_current_user_partial(self, client: TestClient, test_db: Session, test_user: User):
        """Test updating current user profile with partial data."""
        access_token = create_access_token(data={"sub": test_user.email})
        headers = {"Authorization": f"Bearer {access_token}"}

        update_data = {
            "first_name": "PartialUpdate"
        }

        response = client.put("/api/v1/users/me",
                              json=update_data, headers=headers)
        assert response.status_code == 200

        data = response.json()
        assert data["first_name"] == "PartialUpdate"
        # Other fields should remain unchanged
        assert data["email"] == test_user.email

    def test_update_current_user_unauthenticated(self, client: TestClient):
        """Test updating current user profile without authentication."""
        update_data = {"first_name": "Should Fail"}
        response = client.put("/api/v1/users/me", json=update_data)
        assert response.status_code == 403

    def test_set_user_goals_success(self, client: TestClient, test_db: Session, test_user: User):
        """Test setting user goals successfully."""
        access_token = create_access_token(data={"sub": test_user.email})
        headers = {"Authorization": f"Bearer {access_token}"}

        goals_data = {
            "daily_calories_target": 2000,
            "daily_protein_target": 150.0,
            "daily_carbs_target": 200.0,
            "daily_fat_target": 80.0
        }

        response = client.post("/api/v1/users/goals",
                               json=goals_data, headers=headers)
        assert response.status_code == 200

        data = response.json()
        assert data["daily_calories_target"] == 2000
        assert data["daily_protein_target"] == 150.0
        assert data["daily_carbs_target"] == 200.0
        assert data["daily_fat_target"] == 80.0

    def test_set_user_goals_partial(self, client: TestClient, test_db: Session, test_user: User):
        """Test setting user goals with partial data."""
        access_token = create_access_token(data={"sub": test_user.email})
        headers = {"Authorization": f"Bearer {access_token}"}

        goals_data = {
            "daily_calories_target": 1800
        }

        response = client.post("/api/v1/users/goals",
                               json=goals_data, headers=headers)
        assert response.status_code == 200

        data = response.json()
        assert data["daily_calories_target"] == 1800

    def test_set_user_goals_unauthenticated(self, client: TestClient):
        """Test setting user goals without authentication."""
        goals_data = {"daily_calories_target": 2000}
        response = client.post("/api/v1/users/goals", json=goals_data)
        assert response.status_code == 403

    def test_update_user_invalid_activity_level(self, client: TestClient, test_db: Session, test_user: User):
        """Test updating user with invalid activity level."""
        access_token = create_access_token(data={"sub": test_user.email})
        headers = {"Authorization": f"Bearer {access_token}"}

        update_data = {
            "activity_level": "invalid_level"
        }

        response = client.put("/api/v1/users/me",
                              json=update_data, headers=headers)
        assert response.status_code == 422  # Validation error

    def test_update_user_invalid_goal(self, client: TestClient, test_db: Session, test_user: User):
        """Test updating user with invalid primary goal."""
        access_token = create_access_token(data={"sub": test_user.email})
        headers = {"Authorization": f"Bearer {access_token}"}

        update_data = {
            "primary_goal": "invalid_goal"
        }

        response = client.put("/api/v1/users/me",
                              json=update_data, headers=headers)
        assert response.status_code == 422  # Validation error

    def test_set_negative_goals(self, client: TestClient, test_db: Session, test_user: User):
        """Test setting negative values for goals."""
        access_token = create_access_token(data={"sub": test_user.email})
        headers = {"Authorization": f"Bearer {access_token}"}

        goals_data = {
            "daily_calories_target": -100,
            "daily_protein_target": -50.0
        }

        # This should still work as we don't have validation constraints
        # In a real app, you might want to add validation for positive values
        response = client.post("/api/v1/users/goals",
                               json=goals_data, headers=headers)
        assert response.status_code == 200

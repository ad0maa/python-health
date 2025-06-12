import pytest
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.db.database import Base, get_db
from main import app
from app.models.user import User
from app.crud.user import create_user
from app.schemas.user import UserCreate


# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_test_db():
    """Override database dependency for testing."""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def test_db():
    """Create a fresh database for each test."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(test_db):
    """Create a test client with database override."""
    app.dependency_overrides[get_db] = lambda: test_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def test_user(test_db):
    """Create a test user."""
    user_data = UserCreate(
        email="testuser@example.com",
        username="testuser",
        password="testpassword123",
        first_name="Test",
        last_name="User",
        age=25,
        height_cm=170.0,
        weight_kg=65.0,
        gender="male"
    )
    user = create_user(test_db, user_data)
    return user


@pytest.fixture
def test_user_2(test_db):
    """Create a second test user."""
    user_data = UserCreate(
        email="testuser2@example.com",
        username="testuser2",
        password="testpassword456",
        first_name="Test2",
        last_name="User2",
        age=30,
        height_cm=175.0,
        weight_kg=70.0,
        gender="female"
    )
    user = create_user(test_db, user_data)
    return user
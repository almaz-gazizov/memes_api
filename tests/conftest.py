import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.main import app as public_api_app
from api.database import Base
from api.dependencies import get_db
from media_service.main import app as media_service_app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


public_api_app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def client_public_api():
    with TestClient(public_api_app) as client:
        yield client


@pytest.fixture(scope="module")
def client_media_service():
    with TestClient(media_service_app) as client:
        yield client

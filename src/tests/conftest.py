import pytest
from app.main import app
from domain.models.task_model import get_session
from fastapi.testclient import TestClient
from resources.seeds import seed_tables
from sqlmodel.engine.create import create_engine
from sqlmodel.main import SQLModel
from sqlmodel.orm.session import Session
from sqlmodel.pool import StaticPool


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        seed_tables(session)
        yield session


@pytest.fixture(name="test_client")
def test_client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

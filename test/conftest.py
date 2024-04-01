import pytest

from app import app


@pytest.fixture
def client():

    app.app.config['TESTING'] = True
    return app.app.test_client()


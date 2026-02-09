import pytest

from config import BASE_URL

@pytest.fixture(scope="session", autouse=True)
def base_url():
    return BASE_URL
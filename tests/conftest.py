import pytest

from utils.base_session import BaseSession


@pytest.fixture(scope="session")
def reqres():
    api_url = "https://reqres.in"
    return BaseSession(api_url)
import pytest
from lib.movie.static import Endpoint, ResponseCount


@pytest.fixture(scope="module")
def endpoint() -> Endpoint:
    return Endpoint()


def test_address(endpoint: Endpoint) -> None:
    assert endpoint.address == "0.0.0.0"


def test_port(endpoint: Endpoint) -> None:
    assert endpoint.port == 7777


def test_debug(endpoint: Endpoint) -> None:
    assert endpoint.debug is False


def test_max_response_count() -> None:
    assert ResponseCount.MAX.value == 10

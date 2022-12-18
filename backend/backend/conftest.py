import pytest
from typing import Generator

from django.test.utils import setup_test_environment


@pytest.fixture(autouse=True)
def setup_test() -> Generator[None, None, None]:
    setup_test_environment()
    yield

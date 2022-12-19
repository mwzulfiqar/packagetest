from pytest import fixture
import pytest

@fixture
def waltest_fixr():
    print("WALTEST_FIXR IS CALLED.")

@pytest.fixture
def waltest_pytestfixr():
    print("WALTEST_PYTESTFIXR IS CALLED.")
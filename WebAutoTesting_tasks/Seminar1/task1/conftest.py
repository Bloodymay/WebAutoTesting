import pytest

@pytest.fixture()
def good_word():
    return "стол"

@pytest.fixture()
def bad_word():
    return "сттолл"

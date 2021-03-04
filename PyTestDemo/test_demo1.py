import pytest


@pytest.mark.smoke
def test_first_program():
    print("Hello")


@pytest.mark.xfail
def test_second_program():
    print("Good morning")


def test_cross_browser(cross_browser):
    print(cross_browser)

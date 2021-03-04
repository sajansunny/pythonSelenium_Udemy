import pytest


#@pytest.mark.smoke
#@pytest.mark.skip
def test_first_program():
    msg = "Hello"
    assert msg == "Hi", "Texts not matching"


def test_second_creditcard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"




import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute first")
    yield
    print("I will be executed last")


@pytest.fixture()
def dataload():
    print("User profile data being created")
    return ["Sajan", "Sunny", "sajansunny.com"]


@pytest.fixture(params=["Chrome", "Firefox", "IE"])
def cross_browser(request):
    return request.param

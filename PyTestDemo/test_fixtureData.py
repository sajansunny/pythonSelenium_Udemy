import pytest


@pytest.mark.usefixtures("dataload")
class TestExample:

    def test_editprofile(self,dataload):
        print(dataload[0])
        print(dataload[1])
        print(dataload[2])

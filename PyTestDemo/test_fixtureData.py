import pytest

from PyTestDemo.baseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample(BaseClass):

    def test_editprofile(self, dataload):
        log = self.getLogger()
        log.info(dataload[0])
        log.info(dataload[2])

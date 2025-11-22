import pytest


@pytest.mark.sanity
def testLogin():
    print("login successful")


@pytest.mark.skip
def testLogoff():
    print("logoff successful")


@pytest.mark.xfail
def testCalculation():
    assert 2 + 2 == 5

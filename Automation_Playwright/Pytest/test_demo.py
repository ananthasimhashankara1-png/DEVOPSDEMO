import pytest

@pytest.fixture
def setup():
    print("set up done.....")
    
    yield
    print("closing the browser")

# @pytest.mark.skip
def test_one(setup):
    print(" running hte frist test case")
    print("checking the retrun is working" ,setup)

def test_two(setup):
    print("running the second test")
    print("checking the retrun is working" ,setup)

def test_three(setup):
    print("running the three test")
    print("checking the retrun is working" ,setup)
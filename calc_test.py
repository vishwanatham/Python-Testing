import sys
sys.path.insert(1, '.')
from calc import add
import pytest


def test_add():
    assert 5 == add(2, 3)

def test_sum():
    assert 6 == sum([1,2,3])

if __name__ == "__main__":
    pytest.main()


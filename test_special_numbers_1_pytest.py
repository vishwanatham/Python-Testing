import pytest
import SpecialNumbers as sn


def test_reverse():
    assert "321" == sn.reverse("123")


def test_polyndrome():
    assert True == sn.is_polyndrome(121)


if __name__ == "__main__":
    pytest.main()

import pytest
import SpecialNumbers as sn

# Params for fixture
# scope (session, package, module, class, function*)
# params
# autouse (True, False*)
# *Default


@pytest.fixture()
def setup():
    print("setup")


def test_reverse(setup):
    assert "321" == sn.reverse("123")


@pytest.mark.usefixtures("setup")
def test_polyndrome():
    assert True == sn.is_polyndrome(121)


if __name__ == "__main__":
    pytest.main()

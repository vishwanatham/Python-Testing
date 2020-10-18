import sys
sys.path.insert(1,'.')
import SpecialNumbers as sn

def test_string_is_reversed():
    assert "radar" == sn.reverse("radar")

def test_number_is_reversed():
    assert "321" == sn.reverse("123")

def test_polyndrome():    
    assert True == sn.is_polyndrome(121)

def test_non_polyndrome():    
    assert False == sn.is_polyndrome(123)

if __name__ == "__main__":
    test_string_is_reversed()
    test_number_is_reversed()
    test_polyndrome()
    test_non_polyndrome()
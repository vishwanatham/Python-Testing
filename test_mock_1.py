from unittest import mock
from datetime import datetime
import sys
from unittest.mock import Mock
sys.path.insert(1, '.')
import mock_1


@mock.patch("mock_1.datetime")
def test_tuesday_treated_as_weekday(dt):
    tuesday = datetime(year=2020, month=10, day=6)   
    dt.today.return_value = tuesday
    assert mock_1.is_weekday()

@mock.patch("mock_1.datetime")
def test_saturday_treated_as_non_weekday(dt):
    saturday = datetime(year=2020, month=10, day=10)   
    dt.today.return_value = saturday
    assert not mock_1.is_weekday()

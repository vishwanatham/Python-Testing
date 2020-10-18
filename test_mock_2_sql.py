from unittest import mock
import sys
sys.path.insert(1,'.')
import mock_2_sql

# odbc.connect
# connection.cursor()
# cursor.execute()
# results.description
# results.fetchall


@mock.patch('mock_2_sql.odbc')
def test_get_emp_name_wih_max_sal(odbc):
    result = mock.Mock()
    result.description = [["name"], ["salary"]]
    result.fetchall.return_value = [["Bob", 300], ["Rob", 200], ["William", 100]]
    cursor = mock.Mock()
    cursor.execute.return_value = result
    connection = mock.Mock()
    connection.cursor.return_value = cursor
    odbc.connect.return_value = connection
    assert "Bob" == mock_2_sql.get_employee_with_highest_salary()
    


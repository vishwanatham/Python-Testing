import pyodbc as odbc

# Get the name of the employee with max Salary


def get_employee_with_highest_salary():
    connection = odbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.16.4.59,1133;DATABASE=EDD;UID=yerravis;PWD=Password1')
    query = "select name, salary from dbo.tbl_employee e (nolock)"
    cursor = connection.cursor()
    results = cursor.execute(query)
    columns = [column[0] for column in results.description]
    result = []
    for row in results.fetchall():
        result.append(dict(zip(columns, row)))
    connection.close()
    emp_name = ""
    max_sal = 0
    for rec in result:
        if int(rec["salary"]) > max_sal:
            max_sal = rec["salary"]
            emp_name = rec["name"]
    return emp_name

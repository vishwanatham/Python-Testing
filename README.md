# Unit Testing in Python

   This will cover about the different aspects of unit testing in python with examples. Any unittest would usually contatin three blocks
        
    1. Assemble
    2. Act
    3. Assert

 Below are the three popular test frameworks available in python...
        
    1. unittest
    2. pytest
    3. nose / nose2 
    
__unittest__
    
[Unittest](https://docs.python.org/3/library/unittest.html) comes as a builtin library with in python. Inorder to write unit tests using this framework we will have to write test case with in a class, and that class has to inherit _TetsCase_ class. In order to do the assertion we have to use the [assert methods](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual) from the TestCase class of unittest module.
    
__pytest__
        
[Pytest](https://docs.pytest.org/en/stable/) is an external library that has to be installed using pip. We can write test cases either with in class or as direct methods without any classes. It uses the default assert statament that comes as part of python.
    
__nose__


### Test Coverage

  [Coverage](https://coverage.readthedocs.io/) module can be used to check the code coverage and generate the reports for the same. These reports basiscally explain which part of the code has been tested and which isn't. 

    # Run pytest with coverage
    python -m coverage run -m pytest -v

    # To check the coverage % in command line
    python -m coverage report SpecialNumbers.py mocking\mock_1.py mocking\mock_2_sql.py

    # To generate the coverage report
    python -m coverage report SpecialNumbers.py mocking\mock_1.py mocking\mock_2_sql.py
  
  see the [documentation](https://coverage.readthedocs.io/en/coverage-5.3/cmd.html) for more command line options

### To work with this in your machine...

    1. Install python 3, or above
    2. Add python location to your path valriable
    3. Run "pip install -r requirements.txt" in root directory
    4. Run "pytest -v -s" to check the result of test cases

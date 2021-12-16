import unittest
from package.add import add_col
from package.add import add_book
from package.add import add_change_value

"""
Unit tests to verify how the code responds to given inputs that are known to be valid, invalid and already in the dataset.
The tests have been created just for the functions that require to enter an input because they directly modify the database which is csv and a problem arises when a value 
containing a comma is inputted and saved since the csv consider a comma as a value separator. Therefore, if a value containing a comma is inputted and saved,
the csv file will not be correctly opened anymore.

There are three tests done one add_col, add_book and add_change_value each time. Those tests are:
- the test_correct_values that checks if the known valid entries are accepted and returns a "changes have been made" message when the test is passed;
- the test_wrong_values that checks if the known invalid errors (those containing a comma) are not accepted as expected. If the tests is passed, a "please, 
  don't insert any comma ',' as new value" message is returned.
- as corner case, the test_already_present_values function that checks if an entry is already in the database and returns a message accordingly: 
  for add_col, if the column we want to add already exits in the database, a "this column is already present in the database" message has to be displayed;
  for add_book, if the book we want to add is already saved, a "this book is already present in the database" has to be displayed.

"""
# create a class
class TestInput(unittest.TestCase):

    # define function to test known valid entries
    def test_correct_values(self):
        
        # create a test function using self.assertEqual for add_col, define the column name input to test inside the brackets, 
        # define the message to be displayed if the test is passed
        self.assertEqual(add_col("copies_sold"), "changes have been made")
        
        # create a test function using self.assertEqual for add_book, define the book name input to test inside the brackets,
        # define the message to be displayed if the test is passed
        self.assertEqual(add_book("a game of thrones"), "changes have been made")
        
        # create a test function using self.assertEqual for add_change_value, define the inputs to test inside the brackets, 
        # define the message to be displayed if the test is passed
        self.assertEqual(add_change_value("divine comedy", "publication_date", "1472"), "changes have been made")

    # define function to test known invalid entries
    def test_wrong_values(self):
       
        # create a test function using self.assertEqual for add_col, specify in the brackets that any string with comma is the values to test, 
        # define the message to be displayed if the test is passed
        self.assertEqual(add_col("any_string_with_comma ',' "), "please, don't insert any comma ',' as new value")
        
        # create a test function using self.assertEqual for add_book, specify in the brackets that any book name with comma is the values to test, 
        # define the message to be displayed if the test is passed
        self.assertEqual(add_book("any_book's_name with comma ',' "), "please, don't insert any comma ',' as new value")
        
        # create a test function using self.assertEqual for add_change_value, define the inputs to test inside the brackets, 
        # define the message to be displayed if the test is passed
        self.assertEqual(add_change_value("it", "publication_date", "any_string_with_comma , "), "please, don't insert any comma ',' as new value")

        
    # define function to test already existing values
    def test_already_present_values(self):
        
        # create a test function using self.assertEqual for add_col, specify in the brackets the column name already existing and that you want to test
        # define the message to be displayed if the test is passed
        self.assertEqual(add_col("publication date"), "this column is already present in the database")
        
        # create a test function using self.assertEqual for add_book, specify in the brackets the book name already existing and that you want to test
        # define the message to be displayed if the test is passed
        self.assertEqual(add_book("it"), "this book is already present in the database")


# lines of code to say that if this document is recalled, it will be run
if __name__ == '__main__':
    unittest.main()


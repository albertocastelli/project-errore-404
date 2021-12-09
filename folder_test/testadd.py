import unittest
from package.add import add_column
from package.add import add_book
from package.add import add_change_value


class TestInput(unittest.TestCase):

    def test_correct_values(self):
        self.assertEqual(add_column("copies_sold"), "changes have been made")
        self.assertEqual(add_book("a game of thrones"), "changes have been made")
        self.assertEqual(add_change_value("divine comedy", "publication_date", "1472"), "changes have been made")

    def test_wrong_values(self):
        self.assertEqual(add_column("any_string_with_comma ',' "),
        "please, don't insert any comma ',' as new value")
        self.assertEqual(add_book("any_book's_name with comma , "),
        "please, don't insert any comma ',' as new value")
        self.assertEqual(add_change_value("it", "publication_date", "any_string_with_comma , "),
        "please, don't insert any comma ',' as new value")

    def test_already_present_values(self):
        self.assertEqual(add_column("publication date"), "this column is already present in the database")
        self.assertEqual(add_book("it"), "this book is already present in the database")
        
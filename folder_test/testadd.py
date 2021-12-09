import unittest
from package.add import add_column
from package.add import add_book
from package.add import add_change_value


class TestInput(unittest.TestCase):

    def test_correct_values(self):
        self.assertEqual(add_column("copies_sold"), "changes have been made")
        self.assertEqual(add_book("a game of thrones"), "changes have been made")
        self.assertEqual(add_change_value("divine comedy", "publication_date", "1472"), "changes have been made")

        
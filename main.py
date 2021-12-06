from package.add import add_book
from package.add import add_col
from package.add import add_change_value
import argparse
import pandas as pd

df = pd.read_csv("data.csv", index_col = 0, dtype = str)

fun = {
"1":add_book,
"2":add_col,
"3":add_change_value
}


parser = argparse.ArgumentParser(description = "Handle the dataset of a library")
parser.add_argument("command", type = str, help = "insert a valid number: '1' for adding a book,"
 "'2' for adding a column,"
, choices=fun.keys())
parser.add_argument("--book", type = str, choices= df["books"], help = "insert a string with the "
"name a valid book")
parser.add_argument("--writer", type = str, choices= df["writers"], help = "insert a string with "
"the name of a valid writer")
parser.add_argument("--n_book", type = str, help = "insert a string with the name of the new book")
parser.add_argument("--n_col", type = str, help = "insert a string with the name of the new column")
parser.add_argument("--n_value", type = str, help = "insert a string with the new value")
args = parser.parse_args()

f = fun[args.command]

if f == add_book:
  f(args.n_book)

elif f == add_col:
  f(args.n_col)

elif f == add_change_value:
  f(args.book, args.col, args.n_value)


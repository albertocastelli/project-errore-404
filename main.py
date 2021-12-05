from package.add import add_book
from package.add import add_col
from package.add import add_change_value
import argparse
import pandas as pd

df = pd.read_csv("data.csv", index_col = 0, dtype = str)

fun={"1":add_book,
"2":add_col,
}


parser=argparse.ArgumentParser(description="Handle the dataset of a library")
parser.add_argument("command",type=str, help="insert a valid number: '1' for adding a book,"
 "'2' for adding a column,"
, choices=fun.keys())
parser.add_argument("--n_book", type = str, help = "insert a string with the name of the new book")
parser.add_argument("--n_col", type=str, help = "insert a string with the name of the new column")

args=parser.parse_args()

f=fun[args.command]

if f==add_book:
  f(args.n_book)

elif f==add_col:
  f(args.n_col)


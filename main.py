from package.add import add_book
from package.add import add_col
from package.add import add_change_value
import argparse
import pandas as pd
from package.show import show_database
from package.show import top_genre
from package.show import top_writers
from package.show import show_database, top_genre, top_writers
from package.find import find_book
from package.find import find_writer

# open the csv file
df = pd.read_csv("data.csv", index_col = 0, dtype = str)

# create a dictionary where each function created in the project is associated to a number in the dictionary
fun = {
"1":add_book,
"2":add_col,
"3":add_change_value,
"4":show_database,
"5":top_genre,
"6":top_writers,
"7":find_writer,
"8":find_book}

# creating the parser for managing the inputs of the functions
parser = argparse.ArgumentParser(description = "Handle the dataset of a library")

# describe positional argument 'command' for choosing the function
# command: string cointaing a number from 1 to 8 as speccified in the dictionary
parser.add_argument("command", type = str, help = "insert a valid number: '1' for adding a book, "
 "'2' for adding a column, "
 "'3' for adding or changing specific values, "
 "'4' for seeing the whole database, "
 "'5' for seeing the top 5 genres, "
 "'6' for seeing the top 5 writers, "
 "'7' to look for a writer or"
 "'8' to look for a book." 
, choices=fun.keys())

# describe optional arguments

# to check if book in the df
parser.add_argument("--book", type = str, choices= list(df["books"]), help = "insert a string with the "
"name of a valid book")

# to check if writer in df
parser.add_argument("--writer", type = str, choices= list(df["writers"]), help = "insert a string with "
"the name of a valid writer")

# to check if column in df
parser.add_argument("--col", type=str, choices= list(df.columns), help="insert a string with the name of a valid column")

# n_value is any value that is a string (whether the string is correct or not is checked in the function)
parser.add_argument("--n_book", type = str, help = "insert a string with the name of the new book")
parser.add_argument("--n_col", type = str, help = "insert a string with the name of the new column")
parser.add_argument("--n_value", type = str, help = "insert a string with the new value")
args = parser.parse_args()


f = fun[args.command]

# if the function is add_book 
if f == add_book:
  # function is called by using argument '--n_book'
  f(args.n_book)

# if the function is add_col
elif f == add_col:
  # function is called by using argument '--n_col'
  f(args.n_col)

# parser argument '--book', '--col', '--n_value'
# first check if there is the book, then if the column we want to change exists, then change value
elif f == add_change_value:
  f(args.book, args.col, args.n_value)

# parser argument '--writer' for function to find a writer
elif f == find_writer:
  f(args.writer)

# parser argument '--book' to find a book 
elif f == find_book:
  f(args.book)

else:
  f()


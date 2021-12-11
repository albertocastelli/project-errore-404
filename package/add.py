import pandas as pd
import numpy as np


def add_col(col):
    # open the data set as df
    df = pd.read_csv(("data.csv"), index_col = 0, dtype = str)
    # take as input a new column and check if it is a string
    if isinstance(col, str):
        # if it is a string, check if there are no commas 
        if "," not in col:
            # if there are no commas, add the column to df
            if col in list (df.columns):
                # if the column already exists in df, do not add it and display a message saying it already exists
                return "this column is already present in the database"
            # if there are no commas and the column is not in df yet, attach the new column to df
            else:
                df[col] = np.nan
                df.to_csv("data.csv")
                # after attaching, return a message that confirms the changes
                return "changes have been made"
        # if there are commas in the column name, return a message saying not to insert commas
        elif "," in col:
            return "please, don't insert any comma ',' as new value"
    #if the name of the new column is no a string, show a message saying that you have to insert a string as value
    elif not isinstance(col, str):
        return "please insert a string with a name for the new column"
    # for other situations, display that the input is not valid
    else:
        return "please insert a valid input"


def add_change_value(book, col, value):
    df = pd.read_csv("data.csv", index_col = 0, dtype = str)
    if book in list(df["books"]) and col in list(df.columns):
        if isinstance(value,str):
            if "," not in value:
                df.loc[df[df["books"]==book].index.tolist()[0], col] = value
                df.to_csv("data.csv")
                return "changes have been made"
            elif "," in value:
                return "please, don't insert any comma ',' as new value"
        elif not isinstance(value,str):
            return "please insert a string with a valid new value"
    else:
        return "please insert valid inputs"


def add_book(n_book):
    df = pd.read_csv("data.csv", index_col = 0, dtype = str)
    if isinstance(n_book,str):
        if "," not in n_book:
            if n_book in list(df["books"]):
                return "this book is already present in the database"
            else:
                df.loc[len(df.index)] = [n_book] + [np.nan for x in range(len(df.loc[0]) - 1)]
                df.to_csv("data.csv")
                return "changes have been made"
        elif "," in n_book:
            return "please, don't insert any comma ',' as new value"
    elif not isinstance(n_book,str):
        return "please insert a string with a name for the new book"
    else:
        return "please insert a valid input"



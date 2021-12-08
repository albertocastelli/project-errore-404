import pandas as pd
import numpy as np


def add_col(col):
    df = pd.read_csv(("data.csv"), index_col = 0, dtype = str)
    df[col] = np.nan
    df.to_csv("data.csv")


def add_book(book):
    df = pd.read_csv(("data.csv"), index_col = 0, dtype = str)
    df.loc[len(df.index)] = [book] + [np.nan for x in range(len(df.loc[0])-1)]
    df.to_csv("data.csv")


def add_change_value(book, col, value):
    df = pd.read_csv("deta.csv", index_col = 0, dtype = str)
    if book in list(df["books"]) and col in list(df.columns):
        if isinstance(value,str):
            if "," not in value:
                df.loc[df[df["book"]==book].index.tolist()[0], col] = value
                df.to_csv("data.csv")
                return "changes have been made"
            elif "," in value:
                return "please, don't insert any comma ',' as new value"
         elif not isinstance(value,str):
            return "please insert a string with a valid new value"
     elif book not in list(df["books"]):
        return "please insert a book that is present in the dataframe"
     elif col not in list(df.columns):
            return "please insert a column present in the dataframe"
     else:
        return "please insert valid inputs"



import pandas as pd
import numpy as np


def add_col(col):
    df = pd.read_csv(("data.csv"), index_col = 0, dtype = str)

    df[col] = np.nan
    df.to_csv("data.csv")


def add_book(book):
    df = pd.read_csv(("data.csv"), index_col =0, dtype = str)
    df.loc[len(df.index)] = [book] + [np.nan for x in range(len(df.loc[0])-1)]
    df.to_csv("data.csv")


def add_change_value(book, col, value):
    df = pd.read_csv("deta.csv", index_col = 0, dtype = str)
    if book in list(df["books"]) and col in list(df.columns):
        df.loc[df[df["book"]==book].index.tolist()[0], col] = value
        df.to_csv("data.csv")
        print("changes have been made")


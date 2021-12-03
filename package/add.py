import pandas as pd
import numpy as np

def add_book(book):
    df = pd.read_csv(("data.csv"), index_col = O, dtype = str)
    df.loc[len(df.index)] = [book] + [np.nan for x in range(len(df.loc[0])-1)]
    df.to_csv("data.csv")

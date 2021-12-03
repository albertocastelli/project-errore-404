import pandas as pd
import numpy as np











def add_col(col):
    df = pd.read_csv(("data.csv"), index_col = O, dtype = str)
    df[col] = np.nan
    df.to_csv("data.csv")

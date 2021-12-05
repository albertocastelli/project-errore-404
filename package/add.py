def add_change_value(book, col, value, verbose = False):
    df = pd.read_csv("deta.csv", index_col = 0, dtype = str)
    if verbose:
        print("we are making the changes you want...")
    if book in list(df["books"]) and col in list(df.columns):
        df.loc[df[df["book"]==book].index.tolist()[0], col] = value
        df.to_csv("data.csv")
        print("changes have been made")

import pandas as pd 

def find_book(book):
    df = pd.read_csv("data.csv", index_col = 0, dtype = str)
    if book in list(df["book"]):
        pos = df[df["book"] == book].index.tolist():
        print(df.iloc[pos,:])
    else: print("Sorry, we do not have book '{}' in our library".format(book))


def find_writer(writer):
    df = pd.read_csv("data.csv", index_col = 0, dtype = str)
    if writer in list(df["writers"]):
        pos_s = df[df["writers"] == writer].index.tolist()
        print(df.iloc[pos_s,:])
    else: print("Sorry, we do not have writer '{}' in our library".format(writer))
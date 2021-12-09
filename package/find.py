import pandas as pd 

def find_book(book):
    df = pd.read_csv("data.csv", index_col = 0, dtype = str)
    if book in list(df["books"]):
        pos = df[df["books"] == book].index.tolist()
        print(df.iloc[pos,:])
    elif book == None:
        print ("please insert a real name of a book")
    else: print("Sorry, we do not have book '{}' in our library".format(book))


def find_writer(writer):
    df = pd.read_csv("data.csv", index_col = 0, dtype = str)
    if writer in list(df["writers"]):
        pos_s = df[df["writers"] == writer].index.tolist()
        print(df.iloc[pos_s,:])
    elif writer == None:
        print ("please insert a real name of a writer")
    else: print("Sorry, we do not have writer '{}' in our library".format(writer))

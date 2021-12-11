import pandas as pd 

def find_book(book):
    """This function allows the user to find out if a specific book is present or not in the dataframe.
    To do this, the function will receive as input the title of the book the user wants to find. 

    If the title of the book exists in the dataframe, the function will show all the information
    related to the searched name.
    If the input entered by the user is invalid, the function will ask them to insert an actual book 
    title.
    If the title of the book does not exist in the dataframe, the function will show a message saying 
    that the searched book was not found.
    """

    df = pd.read_csv("data.csv", index_col = 0, dtype = str)
    if book in list(df["books"]):
        pos = df[df["books"] == book].index.tolist()
        print(df.iloc[pos,:])
    elif book == None:
        print ("please insert a real name of a book")
    else: print("Sorry, we do not have book '{}' in our library".format(book))


def find_writer(writer):
    """This function allows the user to find out if a specific writer is present or not in the dataframe.
    To do this, the function will receive as input the name of the author the user wants to find.

    If the name of the writer is present in the dataframe, the function will show all the books the
    searched author has written.
    If the input entered by the user is invalid, the function will ask them to insert an actual writer
    name.
    If the name of the writer is not present in the dataframe, the function will show a message saying 
    that the searched author was not found.
    """

    df = pd.read_csv("data.csv", index_col = 0, dtype = str)
    if writer in list(df["writers"]):
        pos_s = df[df["writers"] == writer].index.tolist()
        print(df.iloc[pos_s,:])
    elif writer == None:
        print ("please insert a real name of a writer")
    else: print("Sorry, we do not have writer '{}' in our library".format(writer))

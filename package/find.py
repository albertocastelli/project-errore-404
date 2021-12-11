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

    # the function opens the dataset as df
    df = pd.read_csv("data.csv", index_col = 0, dtype = str)
    # the function takes as input the title of the book
    # if the book is present in the dataframe
    if book in list(df["books"]):
        # pos memorises the row where the searched book is present
        pos = df[df["books"] == book].index.tolist()
        # the function shows all information contained in the dataframe related to the book
        print(df.iloc[pos,:])
    # if the input is invalid
    elif book == None:
        # the function asks to insert an actual book title
        print ("please insert a real name of a book")
    # if the book is not present in the dataframe
    else: 
        # the function prints the following message
        print("Sorry, we do not have book '{}' in our library".format(book))


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

    # the function opens the dataset as df
    df = pd.read_csv("data.csv", index_col = 0, dtype = str)
    # the function takes as input the name of the author
    # if the writer is present in the dataframe
    if writer in list(df["writers"]):
        # pos_s memorises the row (or rows) where the writer is present
        pos_s = df[df["writers"] == writer].index.tolist()
        # the function shows all the books that the searched author has written
        print(df.iloc[pos_s,:])
    # if the input is invalid
    elif writer == None:
        # the function asks to insert an actual writer name
        print ("please insert a real name of a writer")
    # if the author is not present in the dataframe
    else: 
        # the function prints the following message
        print("Sorry, we do not have writer '{}' in our library".format(writer))

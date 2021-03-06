import pandas as pd
import numpy as np


def add_col(col):
    """ This function allows the user to insert a new column  to the dataframe loaded.
    Before being able to actually insert the new column, some aspects have to be checked:
    - if the input is a string
    - if it contains commas
    - if it already exists in the dataframe
    
    If the column name already exists in the dataframe, it will not be added;
    if the column name is not a string, the user will be asked to insert a string value;
    if the the column name is a string, does not exist in the dataframe but has a comma in the name, 
       the user will be asked to change the column name to one without commas;
    if the column name is a string, does not exist in the framework and has no commas in the name, 
       it will be added to data.csv;
    for any other instance of invalidity, a message saying to insert a valid input will be dispalyed.
    """
    
    # open the dataset as df
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
    """ This function allows the user to add or change specific information inside a cell of the dataframe.
    
    The function needs 3 inputs:
    - book: the book on which the user wants to make changes;
    - col: the column in which the user wants to make changes;
    - value: the values the users wants to put in the cell.
    The accepted 'book' values are the books that are already present in the column "books". 
    The accepted 'col' values are the names of the columns already present in the dataset.
    The accepted 'value' values are all the strings which do not contain any commas, since introducing any comma
    would change the behavior of the data.csv
    """
    # The function opens the dataset
    df = pd.read_csv("data.csv", index_col = 0, dtype = str)
    # It checks whether 'book' and 'col' are present in the dataset.
    # If they are present, the function proceeds. Otherwise it
    # prints that there are some problems
    if book in list(df["books"]) and col in list(df.columns):
        # Checks if 'values' is a string, important for the correct functioning of the code
        if isinstance(value,str):
            # Checks if 'value' has a ',' inside of it because in such case the function won't work
            if "," not in value:
                # In case everything is alright, the function will work correctly, changing the 
                # given cell with the new 'value' inserted by the user and printing the following
                # message: " changes have been made "
                df.loc[df[df["books"]==book].index.tolist()[0], col] = value
                df.to_csv("data.csv")
                return "changes have been made"
            elif "," in value:
                # If it finds any comma, it will ask the user not to use any
                return "please, don't insert any comma ',' as new value"
        elif not isinstance(value,str):
            return "please insert a string with a valid new value"
    else:
        return "please insert valid inputs"


def add_book(n_book):
    """ This function allows the user to insert a new book to the dataframe loaded.
    Before being able to actually insert the new book, some aspects have to be checked:
    - if the input is a string
    - if it contains commas
    - if it already exists in the dataframe
    
    If the book name already exists in the dataframe, it will not be added;
    if the book name is not a string, the user will be asked to insert a string value;
    if the the book name is a string, does not exist in the dataframe but has a comma in the name, 
       the user will be asked to change the book name to one without commas;
    if the book name is a string, does not exist in the framework and has no commas in the name, 
       it will be added to data.csv, under the column name 'books', and the other related columns
       (ie writers) will be left with a nan value;
    for any other instance of invalidity, a message saying to insert a valid input will be dispalyed.
    """
    # open the data set as df
    df = pd.read_csv("data.csv", index_col = 0, dtype = str)
    # take a new book title and check if it is a string
    if isinstance(n_book,str):
        # if it is a string and there are no commas in the name
        if "," not in n_book:
            # if the book title is alredy in df 
            if n_book in list(df["books"]):
                # return a message saying that is it already in df
                return "this book is already present in the database"
            # if book title not in df yet
            else:
                # add the book title to column 0 'books' + insert nan values to the rest of the row wrt other columns (ie writers, genre)
                df.loc[len(df.index)] = [n_book] + [np.nan for x in range(len(df.loc[0]) - 1)]
                # attach changes to csv and return message of changes succefully made
                df.to_csv("data.csv")
                return "changes have been made"
        # if there are commas in the book title
        elif "," in n_book:
            # return the following message
            return "please, don't insert any comma ',' as new value"
    # if the input is not a string, return a message saying to insert a string as input
    elif not isinstance(n_book,str):
        return "please insert a string with a name for the new book"
    # for other situations, display that the input is not valid
    else:
        return "please insert a valid input"



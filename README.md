# project-errore-404

## description
The dataset selected for the development of our project work was 'library'. The original dataframe contained 10? books and three columns: books, writers, genre.
The main aim of the project was to create functions that would enable the user to manually add elements to the dataframe and modify it as well.

### add_col()
The add_col function enables users to add any new column to the dataframe. However, before being able to actually attch the new column, some criterias have to be checked:
- if the input is a string
- if it contains commas
- if it already exists in the dataframe


Indeed, if the column name already exists in the dataframe, it will not be added;

if the column name is not a string, the user will be asked to insert a string value;

if the the column name is a string, does not exist in the dataframe but has a comma in the name, the user will be asked to change the column name to one without commas;

if the column name is a string, does not exist in the framework and has no commas in the name, it will be added to data.csv;

whilst for any other instance of invalidity, a message saying to insert a valid input will be dispalyed.

### add_book()
The same reasoning and logic is applied to the add_book function. the aim of this function is to add a new row with the book name under the 'books' column, and add 'nan' to all the other columns (ie writers) in the same row. Also in thi case, commas, string inputs and existance in the dataframe have to be checked.

If the book name already exists in the dataframe, it will not be added;

if the book name is not a string, the user will be asked to insert a string value;

if the the book name is a string, does not exist in the dataframe but has a comma in the name, the user will be asked to change the book name to one without commas;

if the book name is a string, does not exist in the framework and has no commas in the name, it will be added to data.csv, under the column name 'books', and the other related columns (ie writers) will be left with a nan value;

for any other instance of invalidity, a message saying to insert a valid input will be dispalyed.

### add_change_value()
This function allows the end user to modify and / or add additional information inside a cell of the dataframe. It basically allows the user to customize his library archive.

    This function needs 3 inputs:
    - book: the book on which the user wants to make changes and here the accepted values are only the names 
    of books that are already present in the archive;
    
    - col: the code refers to the column in which the user wants to make changes and the accepted values 
    are only columns names already present in the dataset;
    
    - value: the values the users wants to put / add / modify in the cell. This is the only new and unknown input that should be 
    written by the user. 
    The accepted values that can be inserted in this case are all the strings which do not contain any commas, 
    since introducing any comma would change the behavior of the data.csv
    
The expected output is an update of the archive with the new/modified information that the user decided to insert.

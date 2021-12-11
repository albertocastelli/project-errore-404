# project-errore-404

## description
The dataset selected for the development of our project work was 'library'. The original dataframe contained 10? books and three columns: books, writers, genre.
The main aim of the project was to create functions that would enable the user to manually add elements to the dataframe and modify it as well.


The add_col function enables users to add any new column to the dataframe. However, before being able to actually attch the new column, some criterias have to be checked:
- if the input is a string
- if it contains commas
- if it already exists in the dataframe
Indeed, if the column name already exists in the dataframe, it will not be added;
if the column name is not a string, the user will be asked to insert a string value;
if the the column name is a string, does not exist in the dataframe but has a comma in the name, the user will be asked to change the column name to one without commas;
if the column name is a string, does not exist in the framework and has no commas in the name, it will be added to data.csv;
whilst for any other instance of invalidity, a message saying to insert a valid input will be dispalyed.

The same reasoning and logic is applied to the add_book function. the aim of this function is to add a new row with the book name under the 'books' column, and add 'nan' to all the other columns (ie writers) in the same row. Also in thi case, commas, string inputs and existance in the dataframe have to be checked.
If the book name already exists in the dataframe, it will not be added;
if the book name is not a string, the user will be asked to insert a string value;
if the the book name is a string, does not exist in the dataframe but has a comma in the name, the user will be asked to change the book name to one without commas;
if the book name is a string, does not exist in the framework and has no commas in the name, it will be added to data.csv, under the column name 'books', and the other related columns (ie writers) will be left with a nan value;
for any other instance of invalidity, a message saying to insert a valid input will be dispalyed.

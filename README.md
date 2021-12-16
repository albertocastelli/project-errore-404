# project-errore-404

## description
The dataset selected for the development of our project work was 'library'. The original dataframe contained 10? books and three columns: books, writers, genre.
The main aim of the project was to create functions that would enable the user to manually add elements to the dataframe and modify it as well.

### show_database()
This function allows the user to open the database and print it. 

### top_writers()
This function enables the user to open the dataframe and to create a new one where it groups values by writers. It counts how many times writers show up and it orders them based 
on how many times they are counted. The function considers only the first five writers. 

In the final part it creates a barplot showing the database.

### top_genre()
Similar to the top_writers() function, also in this case the user can open the dataframe and create a new one where it groups values by genre. It counts how many times genres show up and it puts them into an order based on how many thimes they are counted. The function takes into consideration only the first five genres.

In the end it creates a barplot showing the database.

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
- book: the book on which the user wants to make changes and here the accepted values are only the names of books that are already present in the archive;
    
- col: the code refers to the column in which the user wants to make changes and the accepted values are only columns names already present in the dataset;
    
- value: the values the users wants to put / add / modify in the cell. This is the only new and unknown input that should be written by the user. 
 The accepted values that can be inserted in this case are all the strings which do not contain any commas, since introducing any comma would change the behavior of the data.csv
    
The expected output is an update of the archive with the new/modified information that the user decided to insert.


### Tests
Unit tests to verify how the code responds to given inputs that are known to be valid, invalid and already in the dataset.
The tests have been created just for the functions that require to enter an input because they directly modify the database which is csv and a problem arises when a value 
containing a comma is inputted and saved since the csv consider a comma as a value separator. Therefore, if a value containing a comma is inputted and saved,
the csv file will not be correctly opened anymore.
There are three tests done one add_col, add_book and add_change_value each time. Those tests are:
- the test_correct_values that checks if the known valid entries are accepted and returns a "changes have been made" message when the test is passed;
- the test_wrong_values that checks if the known invalid errors (those containing a comma) are not accepted as expected. If the tests is passed, a "please, don't insert any comma ',' 
  as new value" message is returned.
- as corner case, the test_already_present_values function that checks if an entry is already in the database and returns a message accordingly: 
  for add_col, if the column we want to add already exits in the database, a "this column is already present in the database" message has to be displayed;
  for add_book, if the book we want to add is already saved, a "this book is already present in the database" has to be displayed.
  
  
### Argparse
Argparse is used to manage the library functions. By calling the 'main' function, it is possible to select the function needed through the command - which is a number between 1 and 8.
Based on the number typed, different functions are called and, consequently, you are asked to type different inputs.
Given the numbers from 1 to 8, the asssociated functions are:
- 1 - add_book
- 2 - add_col
- 3 - add_change_value
- 4 - show_database
- 5 - top_genre
- 6 - top_writers
- 7 - find_writer
- 8 - find_book

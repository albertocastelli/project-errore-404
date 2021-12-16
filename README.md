# project-errore-404

## Description of the project
The dataframe contains information regarding several books, more specifically the title, the author name, the publication date, and the genre.

The aim of the project was creating a set of functions thanks to which the user can add, modify, find, and analyse data contained in the dataframe. Based on the type of function, specific inputs are needed to make it work.

## How does it work
The user can select what to do by typing a number between 1 and 8. To each of these numbers a function, and consequently a specific action, is associated:
- 1 : add_book function. The user can add a new book to the dataframe by inserting its title;
- 2 : add_col function. The user can add a new column to the dataframe;
- 3 : add_change_value function. The user can modify and/or add new information inside an already existing cell of the dataframe;
- 4 : show_database function. The user can open and print the dataframe;
- 5 : top_genre function. The user can see which are the top 5 genres present in the dataframe;
- 6 : top_writers function. The user can see which are the top 5 writers present in the dataframe;
- 7 : find_writer function. The user can see all the books written by a specific author by typing the name of a writer;
- 8 : find_book function. The user can see all the information (author, publication date, and genre) related to a specific book by typing its title.

## Tests
Some unit tests have been implemented to verify how the code responds to different inputs, namely those that are known to be valid, invalid and already present in the dataframe.

They have been created just for the functions requiring to enter an input that will directly modify the dataframe. This is because csv files are sensitive to values containing commas, since they can create some problems. If the user enters such values as inputs, after they are saved the file will not open correctly anymore.

These tests can be run only once. After adding the new values, which ahve been passed to verify the correct behaviour of the functions, the changes made are permanently saved, thus making it impossible to repeat them.
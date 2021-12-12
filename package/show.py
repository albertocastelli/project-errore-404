import pandas as pd
import matplotlib.pyplot as plt

def show_database():
  """ This function allows the user to open the database and print it.
  """
  # The function opens the dataset
  df=pd.read_csv("data.csv", index_col = 0, dtype = str)
  # It prints the dataset
  print(df)

def top_writers():
  """ The function opens the dataframe and it creates a new dataframe, where it groups values by writer. It counts how many times writers show up and it puts them into an order
  based on how many times they are counted. It takes into consideration only the first five writers. 
  In the end it creates a barplot showing the database.
  """
  # The function opens the dataframe
  df = pd.read_csv("data.csv", index_col=0, dtype=str)
  # Creating the dataframe 
  # It counts and order writers based on how many times they are counted
  df_count = df.groupby("writers").count().sort_values(
    # It considers only the first five writers
    "books", ascending = False).iloc[:5, :1]
  # Creating the plot
  fig = plt.figure(figsize = (10,5))
  # Creating a barplot showing the database
  plt.bar(x = df_count.index, height = df_count["books"],
  color = ["c", "orange", "c", "orange", "c"])
  # Showing the barplot
  plt.show()
  print(df_count.T)
        
def top_genre():
  """ The function opens the dataframe and it creates a new dataframe, where it groups values by writer. It counts how many times writers show up and it puts them into an order
  based on how many times they are counted. It takes into consideration only the first five writers. 
  In the end it creates the graph showing the database.
  """
   # The function opens the dataframe
  df = pd.read_csv("data.csv", index_col=0, dtype=str)
  # Creating the dataframe
  # It counts and order genres based on how many times they are counted
  df_count = df.groupby("genre").count().sort_values(
    # It considers only the first five genres
    "books", ascending = False).iloc[:5, :1]
  # Creating the plot
  fig = plt.figure(figsize = (10,5))
  # Creating a barplot showing the database
  plt.bar(x = df_count.index, height = df_count["books"],
  color = ["c", "orange", "c", "orange", "c"])
  # Showing the barplot
  plt.show()
  print(df_count.T)
        

import pandas as pd
import matplotlib.pyplot as plt

def show_database():
  df=pd.read_csv("data.csv", index_col = 0, dtype = str)
  print(df)

def top_writers():
  df = pd.read_csv("data.csv", index_col=0, dtype=str)
  #creating the dataframe
  df_count = df.groupby("writers").count().sort_values(
    "books", ascending = False).iloc[:5, :1]
    #creating the plot
  fig = plt.figure(figsize = (10,5))
  plt.bar(x = df_count.index, height = df_count["books"],
  color = ["c", "orange", "c", "orange", "c"])
  plt.show()
  print(df.count.T)
        
def top_genre():
  df = pd.read_csv("data.csv", index_col=0, dtype=str)
  #creating the dataframe
  df_count = df.groupby("genre").count().sort_values(
    "books", ascending = False).iloc[:5, :1]
  #creating the plot
  fig = plt.figure(figsize = (10,5))
  plt.bar(x = df_count.index, height = df_count["books"],
  color = ["c", "orange", "c", "orange", "c"])
  plt.show()
  print(df.count.T)
        

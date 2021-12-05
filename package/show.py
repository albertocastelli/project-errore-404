def show_database():
    df=pd.read_csv("data.csv", index_col = 0, dtype = str)
    print(df)

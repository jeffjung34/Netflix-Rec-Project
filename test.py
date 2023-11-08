import pandas as pd

#testing

file_name = "Dataset/Netflix_Dataset_Movie.csv"

df = pd.read_csv(file_name)

print(df.head(3))
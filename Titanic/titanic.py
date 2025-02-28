import pandas as pd

# Reads the train.csv file and sets it equal to a variable
titanic_data = pd.read_csv("./train.csv")

# Prints the top bit of the data set
print(titanic_data.head())

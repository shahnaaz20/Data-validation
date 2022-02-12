import json
import pandas as pd
import matplotlib.pyplot as plt


# Uncomment to see the results of file 1
df = pd.read_csv('10_Property_stolen_and_recovered.csv')

# Uncomment to see the results of file 1
# df = pd.read_csv('20_Victims_of_rape.csv')

# Uncomment to see the results of file 1
# df = pd.read_csv('25_Complaints_against_police.csv')

# Uncomment to see the results of file 1
# df = pd.read_csv('28_Trial_of_violent_crimes_by_courts.csv')


print()

# 1. Number of Columns
list_of_column_names = list(df.columns)
print("Number of Columns: ",len(list_of_column_names))
print('-----------------------')


# 2. DataType of columns
Type = dict(df.dtypes)
print(Type)
print('-----------------------')


# 3. checking the blank rows
print(df.isnull().sum())
print('-----------------------')


# 4. identify the key columns.
print(list(df.columns))
print(df.shape)

# 5. Identify the columns which are containing null/blank cells
blank = df.dropna(how="any").shape


plt.title("File Analysis")
plt.xlabel("null/blank cells")
plt.ylabel("Columns")
plt.plot(len(list_of_column_names))
plt.grid(True, linewidth= 1, linestyle="--")
plt.plot(blank)
plt.show()

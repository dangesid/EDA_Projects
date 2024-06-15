import pandas as pd
import numpy as np


# Loading Training dataset
df_train = pd.read_excel("../datasets/Data_Train.xlsx")
df_train.head()

# Loading testing Dataset
df_test = pd.read_excel("../datasets/Test_set.xlsx")
df_test.head()

# Concatenating both the datasets for consistent feature extraction
df_test['Price'] = np.nan  # Adding Price column to the test set for concatenation
df = pd.concat([df_train, df_test], axis=0)

df.head()
print(df.shape)
print(df.columns)
df.info()

# Feature extraction or feature engineering
# Extracting features from Date_of_Journey
df["Date"] = df["Date_of_Journey"].str.split('/').str[0]
df['Month'] = df["Date_of_Journey"].str.split('/').str[1]
df['Year'] = df["Date_of_Journey"].str.split('/').str[2]

# Dropping Date_of_Journey
df = df.drop(["Date_of_Journey"], axis=1)
df.head()

# Converting Date, Month, and Year into int dtype
df["Date"] = df["Date"].astype(int)
df["Month"] = df["Month"].astype(int)
df["Year"] = df["Year"].astype(int)
df.info()

# Removing the date from the arrival time
df["Arrival_Time"] = df["Arrival_Time"].str.split(" ").str[0]

df["Arrival_Hours"] = df["Arrival_Time"].str.split(":").str[0]
df["Arrival_Mins"] = df["Arrival_Time"].str.split(":").str[1]

# Converting Arrival_Hours and Arrival_Mins to int
df["Arrival_Hours"] = df["Arrival_Hours"].astype(int)
df["Arrival_Mins"] = df["Arrival_Mins"].astype(int)

# Dropping Arrival_Time
df = df.drop(["Arrival_Time"], axis=1)
df.head()

# Same processing with Dep_Time
df["Dept_Hours"] = df["Dep_Time"].str.split(":").str[0]
df["Dept_Mins"] = df["Dep_Time"].str.split(":").str[1]

df["Dept_Hours"] = df["Dept_Hours"].astype(int)
df["Dept_Mins"] = df["Dept_Mins"].astype(int)

df.drop(["Dep_Time"], axis=1, inplace=True)
df.head()

# Handling Total_Stops
df["Total_Stops"] = df['Total_Stops'].map({'non-stop': 0, "1 stop": 1, '2 stops': 2, "3 stops": 3, "4 stops": 4})

# Dropping Route
df.drop(["Route"], axis=1, inplace=True)
df.head()

# Checking unique values in Additional_Info
df['Additional_Info'].unique()

# Converting Duration into hours and minutes
df["Duration_Hour"] = df["Duration"].str.extract('(\d+)h').fillna(0).astype(int)
df["Duration_Min"] = df["Duration"].str.extract('(\d+)m').fillna(0).astype(int)

# Total duration in minutes
df["Duration_Total_Min"] = df["Duration_Hour"] * 60 + df["Duration_Min"]

# Dropping Duration
df.drop(["Duration"], axis=1, inplace=True)
df.head()

# Label encoding categorical features
from sklearn.preprocessing import LabelEncoder

labelEncoder = LabelEncoder()
df["Airline"] = labelEncoder.fit_transform(df["Airline"])
df["Source"] = labelEncoder.fit_transform(df["Source"])
df["Destination"] = labelEncoder.fit_transform(df["Destination"])
df["Additional_Info"] = labelEncoder.fit_transform(df["Additional_Info"])

# Separating the combined dataframe back into train and test sets
df_train = df[~df['Price'].isna()]
df_test = df[df['Price'].isna()]

# Dropping the Price column from the test set since it's the target variable for the train set
df_test = df_test.drop(['Price'], axis=1)

# Creating dummy variables for categorical features
df_train = pd.get_dummies(df_train, columns=["Airline", "Source", "Destination", "Additional_Info"], drop_first=True)
df_test = pd.get_dummies(df_test, columns=["Airline", "Source", "Destination", "Additional_Info"], drop_first=True)

# Ensuring the train and test sets have the same dummy variable columns
df_test = df_test.reindex(columns=df_train.columns, fill_value=0)

# Dropping the Price column from the test set again to ensure it's not included accidentally
df_test = df_test.drop(['Price'], axis=1)

# Displaying the processed dataframes
print(df_train.head())
print(df_test.head())

# Showing the final information
print(df_train.info())
print(df_test.info())

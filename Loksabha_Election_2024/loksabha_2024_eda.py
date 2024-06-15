import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/LokSabha_Election_2024_Tweets.csv")

print(df.shape)

df.head(1)

df.info()

sns.histplot(df['No_of_likes'], kde=True)
plt.title('Distribution of Number of Likes')
plt.show()

print(df.columns)

print(df['date'].shape)

len(df['date'].unique())

# now we know there are 663 unique. dates in date column out of 100

df["date"].head()

df["Month"] = df['date'].str.split(" ")

print(df['date'].str.split(" ").str[1])

print(df["date"].str.split("·").str[1])

df.isnull().sum()

df["Date"] = df["date"].str.split(" ").str[1]
df['Month'] = df["date"].str.split(" ").str[0]
df["Year"] = df["date"].str.split(" ").str[2]
df["Hours"] = df["date"].str.split("·").str[1]

df["Tarikh"] = df["Date"].str.replace(','," ", regex=False)

df.head()

df_1 = df.drop("Date",axis=1)

df_1.head()

df = df_1.rename(columns={"Tarikh":"Date"})

df.head()

df["hours"] = df["Hours"].str.split(":").str[0]
df["Minutes"] = df["Hours"].str.split(":").str[1]
df.head()

df["mins"] = df["Minutes"].str.split(" ").str[0]
df["AM/Pm"] = df["Minutes"].str.split(" ").str[1]
df["timestamp"] = df["Minutes"].str.split(" ").str[2]
df = df.drop(["date","Hours","Minutes"],axis=1)

df.head(1)

df.info()

df.head()

"""#Data Visualisation"""

print(df.columns)

first_statement = df["text"][0]

print(df["text"])

def remove_special_chars(text):

  for ch in ['.',',','%','(',')','-',',','&']:
    if ch in text:
      text = text.replace(ch, '')
  return text


df["text"] = df["text"].astype(str).apply(remove_special_chars)

print(df['text'][2])

df['text'].isnull().sum()

print(df["text"].dtype)

df["text"] = df["text"].apply(str)
df['text'].info()

df.info()

df["text"] = df["text"].str.split()

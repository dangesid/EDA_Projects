import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'/content/zomato.csv',encoding= 'latin-1')

df.head(5)

print(df.columns)

print(df.shape)

# finding missing value in a dataset

df.isnull().sum()

# only "cusines" have 9 missing value

# we can use list comprehension to check the missing values

columns_with_missing_values = [features for features in df.columns if df[features].isnull().sum()>0]
print(columns_with_missing_values)

df_country = pd.read_excel("/content/Country-Code.xlsx")

df_country.head()

df.columns

# combine 2 df

final_df = pd.merge(df,df_country,on="Country Code",how="left")

final_df.head(2)

print(final_df.dtypes)

print(final_df.columns)

# how many records are there with respect to country

country_names = final_df.Country.value_counts().index

# from this record we can say zomato is mostly available in india as compared to other country so max number of transactions will be from india
print(country_names)

country_values = final_df.Country.value_counts().values

print(country_values)

# Pie Chart - top 3 countries to use zomato

plt.pie(country_values[:3],labels=country_names[:3],autopct="%1.2f%%")

# this will help me to know how my data is distributed

# Observations : Max transactions or orders for Zomato is from India then followed by USA and UK

print(final_df.columns)

# Now we need to see from which country more rating is there

final_df.groupby(["Aggregate rating","Rating color", 'Rating text']).size()

# Convert the above observation into Dataframe

final_df.groupby(["Aggregate rating","Rating color", 'Rating text']).size().reset_index()

# We see aggregating rating as 0 we have 2140 records and similarly for 4.7 aggregating rating we have 42 records
# removing the 0 from the header and replaceing it with valid name like : No. of ratings

ratings =final_df.groupby(["Aggregate rating","Rating color", 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'})

print(ratings)

# ## Obsservations
# 1. Whenever Rating is from 4.5 to 4.9 rating is excellent
# 2.  Whenever Rating is from 4.0 to 4.4 rating is very Good
# 3. Whenever Rating is from 3.5 to 3.9 rating is Good
# 4.  Whenever Rating is from 2.5 to 3.4 rating is Average
# 5.  Whenever Rating is from 1.8 to 2.2 rating is poor

ratings.head()

plt.rcParams['figure.figsize'] = (12,6)
sns.barplot(x="Aggregate rating",y="Rating Count",hue='Rating color' ,data=ratings)

# since the bar colors and the colors in the data is not matched we can match it using the below way

plt.rcParams['figure.figsize'] = (12,6)
sns.barplot(x="Aggregate rating",y="Rating Count",hue='Rating color',data=ratings,palette=['white','red','orange','yellow','green','green'])

# # observations
#  1. Not Rated count is very high
#  2. Max number of rating is betwwen 2.5 to3.4

final_df.head(5)

# find the country that has given 0 rating

final_df.groupby(["Aggregate rating",'Country']).size().reset_index().head(5).rename(columns={0:'Rating Count'})

# final_df[final_df["Rating color"] == 'white'].groupby('Country').size().reset_index().head(5)

# Observations

#  1. So from the  above data we see max number of 0 ratings are from India

# find out which currency is used by which country

print(final_df.columns)

final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()

# Which country do have online delivery option

final_df[final_df['Has Online delivery']=='Yes'].Country.value_counts()

final_df[['Country','Has Online delivery']].groupby(['Country','Has Online delivery']).size().reset_index().rename(columns={0:''})

# Observations

## Online Delivery are availabale in INDIA and UAE

## Create a pie chart for cities distribution

print(final_df.columns)

print(final_df.City.value_counts().index)

city_values = final_df.City.value_counts().values
city_labels = final_df.City.value_counts().index

plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')

# Find the top 10 cusines

print(final_df.columns)

print(final_df["Cuisines"][:10])


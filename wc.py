import pandas as pd
import numpy as np




df = pd.read_csv("halfclean(5).csv", encoding="ISO-8859-1")

"""df["City"]=df["City"].apply(str)
df["City"]=df["City"].str.lower()
df["City"]=df["City"].str.replace(',nh','').replace('nh','')

df["Price"] = df["Price"].str.replace('$','')

df["Title"] = df["Title"].str.lower()
df["Title"] = df["Title"].str.replace('*','')
df["Title"] = df["Title"].str.replace('?','')
df["Title"] = df["Title"].str.replace('!','')
df["Title"] = df["Title"].str.replace('@','')
df["Title"] = df["Title"].str.replace('&','')
df["Title"] = df["Title"].str.replace('~','')

df["bedroom"]= df["bedroom"].str.replace('br','')

df["ft"]= df["ft"].str.replace('ft2','')

df.to_csv("halfclean.csv", encoding='utf-8', index=False)"""

print(df.head(100))


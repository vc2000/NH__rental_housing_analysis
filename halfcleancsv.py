import pandas as pd
import numpy as np

# nh towns and cities
tc_list = []
with open("nh_town_city.txt") as file:
    for line in file:
        tc_list.append(line.replace("\n", "").lower())


df = pd.read_csv("original-houses.csv")

df["City"] = df["City"].apply(str)
df["City"] = df["City"].str.lower()
df["City"] = df["City"].str.replace(",nh", "").replace("nh", "")

df["Price"] = df["Price"].str.replace("$", "")

df["Title"] = df["Title"].str.lower()
df["Title"] = df["Title"].str.replace("*", "")
df["Title"] = df["Title"].str.replace("?", "")
df["Title"] = df["Title"].str.replace("!", "")
df["Title"] = df["Title"].str.replace("@", "")
df["Title"] = df["Title"].str.replace("&", "")
df["Title"] = df["Title"].str.replace("~", "")

df["bedroom"] = df["bedroom"].str.replace("br", "")

df["ft"] = df["ft"].str.replace("ft2", "")

df.to_csv("halfclean.csv", encoding="utf-8", index=False)

print(df.head(100))

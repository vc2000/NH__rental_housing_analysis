import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


df = pd.read_csv("halfclean(11).csv", encoding="ISO-8859-1")
print(df.head(10))

"""
price per city or town
"""
avg_price_city = df.groupby(["City"])["Price"].mean()

avg_price_city.to_csv("avg_price_city.csv", encoding="utf-8")


"""
    Median price for each city
"""
median_price_city = df.groupby(["City"])["Price"].median()
print(median_price_city)
median_price_city.to_csv("median_price_city.csv", encoding="utf-8")

"""
    Average price per ft for each city
    *** use new dataset that remove null "ft"
"""

avg_price_per_ft_in_city = df.groupby(["City"])["price_per_ft"].mean()
avg_price_per_ft_in_city.to_csv("avg_price_per_ft_in_city.csv", encoding="utf-8")


"""
    Average price per bedroom for each city
    *** use new dataset that remove null "bedroom"
"""

avg_price_per_ft_in_city = df.groupby(["City"])["price_per_br"].mean()
avg_price_per_ft_in_city.to_csv("avg_price_per_bedroom_in_city.csv", encoding="utf-8")

"""
    Number of garage that apartment offer
"""

num_garage = str(df.Title.str.count('garage').sum())

with open("num_garage.txt", "w") as text_file:
    print(f"Number of garage that apartment offer : {num_garage}", file=text_file)

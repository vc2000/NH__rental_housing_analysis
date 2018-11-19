import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


df = pd.read_csv("halfclean(10).csv", encoding="ISO-8859-1")
#print(df.head(10))

"""
price per city or town
"""
avg_price_city=df.groupby(['City'])['Price'].mean()

avg_price_city.to_csv("avg_price_city.csv", encoding='utf-8')


"""
    (63) number of apt offer garage
"""
#print (df.Title.str.count('garage').sum())

"""
    Median price for each city - question?
"""
median_price_city = df.groupby(['City'])['Price'].median()
print(median_price_city)
median_price_city.to_csv("median_price_city.csv", encoding='utf-8')

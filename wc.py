import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator



df = pd.read_csv("halfclean(5).csv", encoding="ISO-8859-1")

ad= df.Title.str.cat(sep=",")


#print(df["Title"].head(10))

wordcloud = WordCloud().generate(ad)

plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
wordcloud.to_file("img/wc_ad_black.png")

wordcloud = WordCloud(
    max_font_size=50, max_words=100, background_color="white"
).generate(ad)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
wordcloud.to_file("img/wc_ad_white.png")
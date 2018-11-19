import requests
import pandas
from bs4 import BeautifulSoup

big_lis = []

i = 0
while i < 3000:
    try:
        if i == 0:
            url = "https://nh.craigslist.org/search/apa"
        else:
            url = "https://nh.craigslist.org/search/apa?s={}".format(i)

        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        all = soup.find_all("li", {"class": "result-row"})

        for items in all:
            d = {}
            d["Title"] = items.find("a", {"class": "result-title hdrlnk"}).text
            try:
                d["City"] = (
                    items.find("span", {"class": "result-hood"})
                    .text.replace(" ", "")
                    .replace("(", "")
                    .replace(")", "")
                )
            except:
                print(None)
            try:
                det = (
                    items.find("span", {"class": "housing"})
                    .text.replace("\n", "")
                    .replace(" ", "")
                    .split("-")
                )
                d["bedroom"] = det[0]
                d["ft"] = det[1]
                # d["Detail"] = detail
            except:
                print(None)
            try:
                d["Price"] = items.find("span", {"class": "result-price"}).text
            except:
                print(None)
            big_lis.append(d)
    except:
        print("stop")
    i += 120

df = pandas.DataFrame(big_lis)
df.to_csv("original-houses.csv")

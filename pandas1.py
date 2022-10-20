import urllib.request
import pandas as pd

url="https://en.wikipedia.org/wiki/List_of_publicly_listed_ITES_companies_of_India"

with urllib.request.urlopen(url) as i:
    html=i.read()

data=pd.read_html(html)[0]
print(data.head())


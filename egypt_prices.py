import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

url = "http://cementegypt.com/en/iron-prices/"
html = urlopen(url)
soup = bs(html, features="html.parser")
all_links = soup.find_all('tr')

list_rows = []

for j in all_links:
    row = j.findAll('td')
    c1 = re.compile('<.*?>')
    clean = (re.sub(c1, '',str(row)))
    list_rows.append(clean)

df = pd.DataFrame(list_rows)
df = df[0].str.split(',', expand = True)
df[0] = df[0].str.strip('[')
df[4] = df[4].str.strip(']')

df.to_csv('05022020.csv')

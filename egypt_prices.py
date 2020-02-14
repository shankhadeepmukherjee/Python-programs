#download rebar prices in Egypt
#import important modules
import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

#open the webpage
url = "http://cementegypt.com/en/iron-prices/"
html = urlopen(url)

#read the html code and row items
soup = bs(html, features="html.parser")
all_links = soup.find_all('tr')

#read the cell elements, strip unrequired items and write to a file
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

df.to_csv('07022020.csv') #change the file name to the date of running the file

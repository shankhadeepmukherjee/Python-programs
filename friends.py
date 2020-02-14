#finds out how many times each of the six main
#characters spoke in the series 'Friends'
#import important modules
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from matplotlib import pyplot as plt

#open the webpage to download the links to the scripts
url = "http://www.livesinabox.com/friends/scripts.shtml"
html = urlopen(url)

#read the html code
soup = bs(html, features="html.parser")

#find out the html references and arrange them
list_links = []

for j in soup.findAll('a'):
    link = j.get('href', None)
    link = "http://www.livesinabox.com/friends/" + str(link)
    list_links.append(link)

#initialise the counters and flag
monica = chandler = pheobe = ross = joey = racheal = 0
i = 45 #this the start index number for the friends scripts in the webpage
#i had created a csv file earlier where the html links were written to identify
#the start and end of the script links

#open each episode script and count the number of times a character spoke
while i < 276:
    html = urlopen(list_links[i])
    soup = bs(html, features="html.parser")
    monica += len(soup.find(text=lambda text: text and 'Monica' in text))
    chandler += len(soup.find(text=lambda text: text and 'Chandler' in text))
    pheobe += len(soup.find(text=lambda text: text and 'Phoebe' in text))
    ross += len(soup.find(text=lambda text: text and 'Ross' in text))
    joey += len(soup.find(text=lambda text: text and 'Joey' in text))
    racheal += len(soup.find(text=lambda text: text and 'Rachel' in text))
    i += 1

#plot the data in a bar graph format
plt.bar(np.arange(6),(monica, chandler, pheobe, ross, joey, racheal))
plt.xticks(np.arange(6), ['Monica','Chandler','Phoebe','Ross','Joey','Rachel'])
plt.yticks([10000,20000,30000,40000,50000])
plt.show()

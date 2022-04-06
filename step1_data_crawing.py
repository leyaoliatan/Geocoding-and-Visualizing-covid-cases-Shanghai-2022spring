#!/usr/bin/env python
# coding: utf-8

# ### Shanghai Covid 2022
# - ***Data crawing***
# - Geocoding
# - Visualizing

# In[3]:


#libraries
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time

# define a function of crawing html
def geturl(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return r.text


# data crawing from the public notice
url = 'https://mp.weixin.qq.com/s/MkKsQkgvUWbwj8z9jG_Zng'
text = geturl(url) #get info from original link
file = open("shanghai0404.txt",'w') #save as a new file
file.write(text) #write info

# parsing
soup = BeautifulSoup(text, "html.parser")
info = soup.find('div', 'rich_media_content')
x = str(info)

# get the infection data as a list
addresses = re.findall('</span></p><p>.*?<span style="font-size: 16px;">([^已<2022].+?)?[，。、<]+?', x)
file = open("shanghai0404_addresses.txt",'w') #save as a new file
for i in addresses:
    file.write(i+'\r') #write info


# get the summary data of all districts
districts = re.findall('2022年4月4日，(.+?区)[无]?新增([\d]+?)?.*?确诊病例，新增([\d]+?)例.*?无症状感染者',x)
li = []
for item in districts:
    di = []
    di.extend(item)
    li.append(di)

df = pd.DataFrame(li,columns=['districts','positive','asymptomatic'])
df.to_csv('shanghai2022_04_04_districts.csv')

print(addresses)
print(districts)
print(df)


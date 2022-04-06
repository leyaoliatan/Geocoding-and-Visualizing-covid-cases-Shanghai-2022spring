#!/usr/bin/env python
# coding: utf-8

# ### Shanghai Covid 2022
# - Data crawing
# - ***Geocoding***
# - Visualizing

# In[12]:


#libraries
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import urllib
import json
import time

# define a function of crawing json from google api
def geturl(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    return r.text

# define a function of parsing json from google api
def getinfo(js):
    i = []
    js = json.loads(text)
    i.append(js['results'][0]['formatted_address'])
    i.append(js['results'][0]['geometry']['location']['lat'])
    i.append(js['results'][0]['geometry']['location']['lng'])
    return(i)


key = 'ENTER YOUR KEY HERE'# replace with your own key copied from google cloud platform


# In[26]:


addresses = open("shanghai0404_addresses.txt",'r').readlines()
print(addresses[0].strip())


data = []
for location in addresses:
    ls = []
    addr = '上海市'+location.strip()
    url = 'https://maps.googleapis.com/maps/api/geocode/json?{}&key={}'.format(urllib.parse.urlencode({'address':addr}), key)
    try:
        text = geturl(url)
    except:
        time.sleep(7)
        try:
            text = geturl(url)
        except:
            text = ''
    try:
        js = json.loads(text)
    except:
        js = None
    if js == None or 'status' not in js or js['status'] != 'OK':
        z = ['','','']
        z.append(addr)
        data.append(z)
        continue
    else:
        z = getinfo(js)
        z.append(addr)
        data.append(z)

df = pd.DataFrame(data,columns=['f_location','latitude','longitude','location'])
df.to_csv('shanghai2022_04_04.csv')


#!/usr/bin/env python
# coding: utf-8

# ### Shanghai Covid 2022
# - Data crawing
# - Geocoding
# - ***Visualizing***

# In[4]:


# libraries

from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


# -------------------------------------
# visualize the summary data of districts

# read the data
df = pd.read_csv('shanghai2022_04_04_districts.csv')

# plot
bar = (
 Bar(init_opts=opts.InitOpts())
 .add_xaxis(list(df.iloc[:,1]))
 .add_yaxis('positive infectors', list(df.iloc[:,2]))
 .add_yaxis('asymptomatic infectors', list(df.iloc[:,3]))
 .set_global_opts(title_opts=opts.TitleOpts(title='Infection data of districts', subtitle = 'Shanghai on 04/04/2022'))
)

bar.render_notebook()


# In[17]:


print(df)


# In[5]:


# -------------------------------------
# visualize the infectors locations data

# first, import the .shp of Shanghai
# import the map
shanghai_map = gpd.read_file('./stanford-dv960kb3448-shapefile/shanghai1.shp')
# plot the empty map
fig,ax = plt.subplots(figsize = (15,15))
shanghai_map.plot(ax = ax, color = 'grey')

# read the data
df = pd.read_csv('shanghai2022_04_04.csv')
crs = {'init': 'epsg:4326'}
# creat points to be shown
geo = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
# gen geodataframe
geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geo)
fig,ax = plt.subplots(figsize = (15,15))

# mark on the map
shanghai_map.plot(ax = ax, color = 'lightgray')
geo_df.plot(ax = ax, markersize = 60, color = 'darkred', alpha = 0.2, marker = 'o')


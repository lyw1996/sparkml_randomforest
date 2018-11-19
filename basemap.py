from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from itertools import chain
import math
import matplotlib as mpl
from mpl_toolkits.basemap import cm
# plt.figure(figsize=(8,8))
# m=Basemap(projection ="lcc",resolution=None,lat_0=50,lon_0=-100,width=8E6,height=8E6)
# m.bluemarble(scale=0.5)
# plt.show()
fig = plt.figure(figsize=(12, 6),edgecolor="w")
fig.suptitle(" Quarter")
ax1 = fig.add_axes([0.05, 0.20, 0.40, 0.75])
ax3 = fig.add_axes([0.50, 0.20, 0.40, 0.75])
ax2 = fig.add_axes([0.05,0.10,0.9,0.05])

m= Basemap(llcrnrlon=-55, llcrnrlat=-25, urcrnrlon=-35, urcrnrlat=-14, projection='lcc', lat_0=-12, lon_0=-40,ax=ax1)
m.readshapefile('gadm36_BRA_shp/gadm36_BRA_1', 'states', drawbounds=True)
m.shadedrelief(scale=0.2)
lats =m.drawparallels(np.linspace(-40,5,13))
lons = m.drawmeridians(np.linspace(-70,-30,13))
lat_lines=chain(*(tup[1][0] for tup in lats.items()))
lon_lines =chain(*(tup[1][0] for tup in lons.items()))
all_lines = chain(lat_lines,lon_lines)
for line in all_lines:
    line.set(linestyle="",alpha=0.3,color="w")
m.drawcountries(linewidth=1.5)
m.drawcoastlines()
#第二张图
m1= Basemap(llcrnrlon=-55, llcrnrlat=-25, urcrnrlon=-35, urcrnrlat=-14, projection='lcc', lat_0=-12, lon_0=-40,ax=ax3)
m1.readshapefile('gadm36_BRA_shp/gadm36_BRA_1', 'states', drawbounds=True)
m1.shadedrelief(scale=0.2)
lats2 =m1.drawparallels(np.linspace(-40,5,13))
lons2 = m1.drawmeridians(np.linspace(-70,-30,13))
lat_lines2=chain(*(tup[1][0] for tup in lats2.items()))
lon_lines2 =chain(*(tup[1][0] for tup in lons2.items()))
all_lines2 = chain(lat_lines2,lon_lines2)
for line in all_lines2:
    line.set(linestyle="",alpha=0.3,color="w")
m1.drawcountries(linewidth=1.5)
m1.drawcoastlines()
ax1.set_title('spring')
ax3.set_title('summer')
city=pd.read_csv("picturemon9.txt",header=None,sep=",",usecols=[0])
lats1=pd.read_csv("picturemon9.txt",header=None,sep=",",usecols=[2])
lots1=pd.read_csv("picturemon9.txt",header=None,sep=",",usecols=[3])
rain=pd.read_csv("picturemon9.txt",header=None,sep=",",usecols=[1])
city_list=city.values.tolist()
citylist=[]
for item in city_list:
    for i in item:
        citylist.append(i)

lats_list=lats1.values.tolist()
latslist=[]
for item in lats_list:
    for i in item:
        latslist.append(i)
lots_list=lots1.values.tolist()
lotslist=[]
for item in lots_list:
    for i in item:
        lotslist.append(i)
rain_list=rain.values.tolist()
rainlist=[]
for item in rain_list:
    for i in item:
        rainlist.append(i)
# print(rainlist)
rainlist_max=max(rainlist)
rainlist_min=min(rainlist)
size_factor=200.0
for i in range(0,len(rainlist)):
    if rainlist[i]<0:
        size=size_factor*abs(rainlist[i])/abs(rainlist_min)
        x,y=m(lotslist[i],latslist[i])
        m.scatter(x,y,s=size,color="red",marker="o")
    elif rainlist[i]==0:
        x,y=m(lotslist[i],latslist[i])
        m.scatter(x, y, s=1, color="red", marker="*")

    else:
        size = size_factor * rainlist[i] / rainlist_max
        x,y=m(lotslist[i],latslist[i])
        m.scatter(x, y, s=size, color="blue", marker="*")
#第二张图
city2=pd.read_csv("picturemon12.txt",header=None,sep=",",usecols=[0])
lats12=pd.read_csv("picturemon12.txt",header=None,sep=",",usecols=[2])
lots12=pd.read_csv("picturemon12.txt",header=None,sep=",",usecols=[3])
rain2=pd.read_csv("picturemon12.txt",header=None,sep=",",usecols=[1])
city_list2=city2.values.tolist()
citylist2=[]
for item in city_list2:
    for i in item:
        citylist2.append(i)
lats_list2=lats12.values.tolist()
latslist2=[]
for item in lats_list2:
    for i in item:
        latslist2.append(i)
lots_list2=lots12.values.tolist()
lotslist2=[]
for item in lots_list2:
    for i in item:
        lotslist2.append(i)
rain_list2=rain2.values.tolist()
# print(rain_list2)
rainlist2=[]
for item in rain_list2:
    for i in item:
        rainlist2.append(i)
print(rainlist2)
rainlist_max2=max(rainlist2)
rainlist_min2=min(rainlist2)
size_factor=200.0
for i in range(0,len(rainlist2)):
    if rainlist2[i]<0:
        size=size_factor*abs(rainlist2[i])/abs(rainlist_min2)
        x,y=m1(lotslist2[i],latslist2[i])
        m1.scatter(x,y,s=size,color="red",marker="o")
    elif rainlist2[i]==0:
        x,y=m1(lotslist2[i],latslist2[i])
        m1.scatter(x, y, s=1, color="red", marker="*")

    else:
        size = size_factor * rainlist2[i] / rainlist_max2
        x,y=m1(lotslist2[i],latslist2[i])
        m1.scatter(x, y, s=size, color="blue", marker="*")

cmap=cm.GMT_polar
norm=mpl.colors.Normalize(vmin=-1,vmax=1)
cb1=mpl.colorbar.ColorbarBase(ax2,cmap=cmap,norm=norm,orientation="horizontal",ticks=[-1,0,1])
cb1.ax.set_xticklabels(["wet","mild","dry"])
plt.show()


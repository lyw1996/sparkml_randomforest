#!/usr/bin/python
# -*- coding :utf-8 -*-
# wsid 天气站id,wsnm,elvt,lat,lon,inme,city,prov,mdct,date,yr,mo,da,hr,prcp降水量,
# stp大气压,smax,smin, gbrd太阳辐射,temp空气温度,dewp,tmax,dmax,tmin,dmin,hmdy相对湿度,hmax,hmin,wdsp风速,wdct,gust
import pandas as pd
import numpy as np
# filepath="sudeste.csv"
# data=pd.read_csv(filepath)
# # 清洗所有含空的数据
#
# data=data[~data['gust'].isin([0.0])]  #
# # print(data)
# data=data.dropna(axis=0)
# print(data)
# data_test=data[data['yr']==2016]
# data_test.to_csv("data_test.csv")
# data_train=data[data['yr']!=2016]
# data_train.to_csv("data_train.csv")
# data[data['prcp']>0]
# print(data[data['yr']!=2016])

# data2=data.dropna(axis=0)
# # data2=data.dropna(axis=0)
# data2.to_csv("data2.csv")
# print(pd.read_csv("data2.csv"))
#
# print(data[['date','prcp']])
# train=np.array(data[['date','prcp']])
# print(train)
# list=train.tolist()
# print(len(list))

filepath="data_train.csv"
data=pd.read_csv(filepath)

data_test=data[data['mo']>9]
data_test.to_csv("data_test12.csv")

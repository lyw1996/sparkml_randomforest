#!/usr/bin/python
# -*- coding :utf-8 -*-
import json
import re
import string
import pandas as pd
import numpy as np
import csv
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import cm
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
fd1=open('picture_ori.txt','w',encoding='utf-8')
fd2=open('picturemon12.txt','w',encoding='utf-8')

f1=open('data_train.csv','r',encoding='utf-8')
csvfile=csv.reader(f1)
rawTrn_data = []
for item in csvfile:
	rawTrn_data.append(item)
f1.close()

f2=open('data_test12.csv','r',encoding='utf-8')
csvfile=csv.reader(f2)
rawTst_data = []
for item in csvfile:
	# print(item)
	rawTst_data.append(item)
f2.close()

f3=open('resultmon12.txt','r',encoding='utf-8')
result=[]
for line in f3:
	# print(line)
	result=line.split(' ')
# print(len(result))
pred_result=[]
for i in range(len(result)):
	if result[i]=='1.0':
		pred_result.append(1.0)
	elif result[i]=='2.0':
		pred_result.append(2.0)
	else:
		pred_result.append(0.0)
# print(len(pred_result))
# datacity
# data=pd.read_csv("data_test.csv")
# data=data['city']
# print(data)
# data_numpy = np.array(data)
# data_list = data_numpy.tolist()
# print(len(data_list))
# data_list=list(set(data_list))
# print(len(data_list))
# print(data_list)
# data_city={}
# for i in range(len(data_list)):
# 	data_city[data_list[i]]=0
data=pd.read_csv("data_test12.csv")
data=data[['city','lat','lon']]
print(data)
data_numpy = np.array(data)
data_list = data_numpy.tolist()
print(len(data_list))
data_jingwei=[]
data_list2=[]
for line in data_list:
	if line not in data_jingwei:
		data_jingwei.append(line)
		data_list2.append(line[0])
print(len(data_jingwei))
print(len(set(data_list2)))
data_city={}
city_jingwei={}
for i in range(len(data_list2)):
	for j in range(len(data_jingwei)):
		print(data_list2[i],data_jingwei[j][0])
		if data_list2[i]==data_jingwei[j][0]:
			city_jingwei[data_jingwei[j][0]]=[data_jingwei[j][1],data_jingwei[j][2]]
			data_city[data_list2[i]]=0

def res_visulization(pred_result):
	popdensity_ori =data_city
	popdensity =data_city
	idx = 0
	# rawTst_data是测试数据
	for i in range(1,len(rawTst_data)):
		user_location = rawTst_data[i][8]
		# print(user_location)
		if float(rawTst_data[i][15])==0:
			# if pred_result[idx]!=0:
			# 	print(False)
			popdensity_ori[user_location] += (0 - 1)
			popdensity[user_location] += (pred_result[idx] - 1)
			idx += 1
		elif float(rawTst_data[i][15])<1:
			popdensity_ori[user_location] += (1 - 1)
			# if pred_result[idx]!=1:
			# 	print(False)
			popdensity[user_location] += (pred_result[idx] - 1)
			idx += 1
		else:
			# if pred_result[idx]!=2:
			# 	print(False)
			popdensity_ori[user_location] += (2 - 1)
			popdensity[user_location] += (pred_result[idx] - 1)
			idx += 1
	print('popdensity_ori')
	for (key,value) in popdensity_ori.items():
		# print(key,value,city_jingwei[key])
		fd1.write(str(key)+','+str(value)+','+str(city_jingwei[key][0])+','+str(city_jingwei[key][1]))
		fd1.write('\n')
	print(popdensity_ori)
	print("---------------------------------------------------------")
	print('popdensity')
	for (key,value) in popdensity.items():
		# print(key,value,city_jingwei[key])
		fd2.write(str(key)+','+str(value)+','+str(city_jingwei[key][0])+','+str(city_jingwei[key][1]))
		fd2.write('\n')
	print(popdensity)
	print("---------------------------------------------------------")



res_visulization(pred_result)


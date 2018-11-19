#!/usr/bin/python
# -*- coding :utf-8 -*-
from __future__ import print_function

import pandas as pd
import numpy as np
from pyspark import SparkContext, SparkConf
from pyspark import SQLContext
from pyspark.mllib.tree import RandomForest
from pyspark.mllib.regression import LabeledPoint



#0 51018 小于0.4 147466 小于1 225399 大于等于1 126449
conf = SparkConf().setAppName("weather_analysis")
sc = SparkContext(conf=conf)
sc.setLogLevel("WARN")
sqlContext = SQLContext(sc)


def readcsv(filepath):
	trn_data=[]
	data = pd.read_csv(filepath)
	# 'stp'大气压,'smax','smin','gbrd'太阳辐射,'temp','dewp'及时露点,'tmax','dmax','tmin','dmin','hmdy'相对湿度,'hmax','hmin','wdsp','wdct','gust']]

	data1=data[['stp','smax','smin','gbrd','temp','dewp','tmax','dmax','tmin','dmin','hmdy','hmax','hmin','wdsp','wdct','gust']]
	# data1 = data[['stp', 'smax', 'smin', 'gbrd',  'wdsp', 'wdct', 'gust']]
	# data1 = data[	[ 'temp', 'dewp', 'tmax', 'dmax', 'tmin', 'dmin', 'hmdy', 'hmax', 'hmin']]

	data_numpy=np.array(data1)
	data_list=data_numpy.tolist()
	# print(len(data_list))
	data2=data[['prcp']]
	data2_numpy=np.array(data2)
	data2_list=data2_numpy.tolist()
	# print(len(data2_list))
	for i in range(len(data_list)):
		# print(type(data2_list[i][0]))
		if data2_list[i][0]==0:
			trn_data.append(LabeledPoint(0, data_list[i]))
		# elif data2_list[i][0]<0.4:
		# 	trn_data.append(LabeledPoint(1, data_list[i]))
		elif  data2_list[i][0]<1:
			trn_data.append(LabeledPoint(1, data_list[i]))
		else:
			trn_data.append(LabeledPoint(2,data_list[i]))
	trnData = sc.parallelize(trn_data)
	print(trnData.collect())
	return trnData

filepath1 = "data_test12.csv"
filepath="data_train.csv"
trnData=readcsv(filepath)
tst_dataRDD=readcsv(filepath1)
model = RandomForest.trainClassifier(trnData, numClasses=3, categoricalFeaturesInfo={},
                                     numTrees=3, featureSubsetStrategy="auto",
                                     impurity='gini', maxDepth=4, maxBins=32)
print('Learned classification tree model:')
print(model.toDebugString())
# print(tst_dataRDD.map(lambda x: x.features))
predictions = model.predict(tst_dataRDD.map(lambda x: x.features))
# print(predictions)
fw=open('resultmon12.txt','w',encoding='utf-8')
for i in predictions.collect():
	fw.write(str(i)+' ')
# labelsAndPredictions = tst_dataRDD.map(lambda lp: lp.label).zip(predictions)
# print(labelsAndPredictions)
# testErr = labelsAndPredictions.filter(lambda (v,p): v != p).count() / float(tst_dataRDD.count())
# print('Test Error = ' + str(testErr))
# visulization the result
print(predictions.collect())
# print(tst_dataRDD.map(lambda x: x.label   ))
# res_visulization(predictions.collect())

sc.stop()
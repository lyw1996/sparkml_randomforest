# sparkml_randomforest
基于spark MLlib 的巴西南部降水量预测
## pre_data.py
对kaggle原始数据进行预处理，并分出训练集和测试集
#### kaggle数据源地址：https://www.kaggle.com/PROPPG-PPG/hourly-weather-surface-brazil-southeast-region ####
## spark_ml.py
提出csv文件中的特征和自定义分类结果，放入random foerest模型中训练，并跑出预测结果
## visualization.py
将预测结果按照城市进行累加，并将城市、结果以及经纬度写入txt，便于绘图
## basemap
使用python的basemap库，画出巴西地图，并根据结果经纬度画出降水量散点图
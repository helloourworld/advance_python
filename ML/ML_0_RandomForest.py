
# coding: utf-8

# 机器学习算法系列教程
# ==================
# 欢迎您的访问！
# 作者：Lijun Yu（davidyjun）大卫君
# 
# 访问网址：[@机器学习_大卫君](http://blog.sina.com.cn/u/2672280861)
# 

### 机器学习算法之随机森林

# 随机森林是数据挖掘中非常常用的分类预测算法，以分类或回归的决策树为基分类器。
# 
# 算法要点：
# >1 each tree in the ensemble is built from a sample drawn with replacement 
# from the trainning set.
# （有限次有放回抽样）
# 
# >2 when splitting a node during the construction of the tree, the split 
# that is chosen is no longer the best split among all features.the split
# that is picked is the best split among a random subset of the features
# （单棵树最好，非全局最好）
# 
# 参考sklearn(http://scikit-learn.org/stable/modules/ensemble.html#random-forests)

# 1.代码示例
# ---------
# 例：以经典的Kaggle"泰坦尼克号"乘客的数据集建模说明。数据[https://www.kaggle.com/c/titanic]

# In[1]:

from model import *


                http://blog.csdn.net/lo_cima/article/details/50533010#
                
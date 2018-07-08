# -*- coding: utf-8 -*-
'''
@Author: fiyc
@Date : 2018-07-08 22:04
@FileName : example_001.py
@Description : 
    - 机器学习算法原理与编程实践 第一个测试代码
    - 用来检验环境是否配置正确
'''

import numpy as np
from numpy import *
import matplotlib.pyplot as plt

# 测试数据集 - 二维list
dataSet = [[-0.017612, 14.053064],
           [-1.395634, 4.662541],
           [-0.752157, 6.538620],
           [-1.322371, 7.152853],
           [0.423363, 11.054667],
           [0.406704, 7.067335],
           [0.667394, 12.741452],
           [-2.46150, 6.866805],
           [0.569411, 9.548755],
           [-0.026632, 10.427743],
           [0.850433, 6.920334],
           [1.347183, 13.175500],
           [1.176813, 3.167020],
           [-1.781871, 9.097953]]

dataMat = mat(dataSet).T # 将数据集转换为Numpy矩阵， 并转置
plt.scatter(dataMat[0].tolist(), dataMat[1].tolist(), c='red', marker='o')

# 绘制直线图形
X = np.linspace(-2, 2, 100)

# 建立线性方程
Y = 2.8 * X + 9

plt.plot(X, Y)
plt.show()
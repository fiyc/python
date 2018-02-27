# -*- coding: utf-8 -*-
from numpy import *


'''
这是《机器学习实战》这本书中, k近邻算法的实现

'''

'''
intX: 用于分类的输入向量
dataSet: 输入的训练样本集
labels: 标签向量(元素数目和dataSet的行数相同)
k: 选择最近邻居的数目
'''
def classify(inX, dataSet, labels, k):

    dataSetSize = dataSet.shape[0]

    # 计算距离
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)

    distances = sqDistances**0.5
    sortedDisIndicies = distances.argsort()
    classCount = {}

    # 选择距离最小的k个点
    for i in range(k):
        votellabel = labels[sortedDisIndicies[i]]
        classCount[votellabel] = classCount.get(votellabel, 0) + 1

    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]


'''
将文本记录转换到NumPy的解析程序
'''


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros(numberOfLines, 3)
    classLabelVector = []

    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1

    return returnMat, classLabelVector


'''
归一化特征值
newValue = (oldValue - min) / (max - min)
'''


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals

    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]

    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))

    return normDataSet, ranges, minVals


'''
分类器针对约会网站的测试代码
'''


def datingClassTest():
    hoRatio = 0.1
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    norMat, ranges, minVals = autoNorm(datingDataMat)
    m = norMat.shape[0]
    numTestVecs = int(m * hoRatio)

    errorCount = 0
    for i in range(numTestVecs):
        classifierResult = classify(norMat[i, :], norMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)

        print "the classifier came back with %d, the real answer is: %d" % (classifierResult, datingLabels[i])

        if(classifierResult != datingLabels[i]):
            errorCount += 1

    print "the total error rate is: %f" % (errorCount / float(numTestVecs))

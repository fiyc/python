# -*- coding: utf-8 -*-
from numpy import *
from os import listdir
import operator
'''
- 机器学习实战
- k-近邻算法
- 手写识别系统
'''

# 将图像转换为测试向量
def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)

    # 这里由于图片资源为32*32, 因此通过两个循环, 将图片的每一点作为特征, 生成一个长度为(1, 1024)的矩阵
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])

    return returnVect

'''
获取输入数据的类型

inX: 输入数据特征
dataSet: 样本数据特征
labels: 样本数据标签
k: 选取前k个最近数据
'''
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDisIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDisIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    sortedClassCount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

'''
手写数字识别系统的测试代码
'''
def handwritingClassTest():
    hwLabels = []
    tranDataPath = '/Users/yif/Desktop/machinelearninginaction/Ch02/digits/trainingDigits'  # 这里是我们存放样本数据的目录
    testDataPath = '/Users/yif/Desktop/machinelearninginaction/Ch02/digits/testDigits'  # 这里是我们存放测试数据的目录
    trainingFifleList = listdir(tranDataPath)
    m = len(trainingFifleList)
    trainingMat = zeros((m, 1024))

    for i in range(m):
        fileNameStr = trainingFifleList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('%s/%s' % (tranDataPath, fileNameStr))

    testFileList = listdir(testDataPath)
    testLength = len(testFileList)
    errorCount = 0.0

    for i in range(testLength):
        firlNameStr = testFileList[i]
        fileStr = firlNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])

        vectorUnderTest = img2vector('%s/%s' % (testDataPath, firlNameStr))
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)

        print "classifier result is: %d, real result is: %d" % (classifierResult, classNumStr)

        if(classifierResult != classNumStr):
            errorCount += 1.0

    print "\nthe total number of error is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount / float(testLength))


if (__name__ == '__main__'):
    handwritingClassTest()

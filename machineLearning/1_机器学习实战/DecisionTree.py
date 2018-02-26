# -*- coding: utf-8 -*-

from math import log


'''
计算给定数据集的香农熵
'''
def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]

		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0

		labelCounts[currentLabel] += 1

	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key]) / numEntries
		shannonEnt -= prob * log(prob, 2)

	return shannonEnt


'''
按照给定特征划分数据集
dataSet: 待划分的数据集
axis: 划分特征的列序号
value: 指定特征的值

该方法会从dataSet中找到所有第axis列的特征值为value的行
并且移除这些行的axis特征后返回
'''
def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reduceFeatVec = featVec[:axis]
			reduceFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reduceFeatVec)

	return retDataSet

'''
选择最好的数据集划分方式
'''
def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0])  - 1 # 获取数据集的特征数量
	baseEntropy = calcShannonEnt(dataSet) # 计算当前数据集的香农熵
	bestInfoGain = 0.0
	bestFeature = -1

	# 遍历所有的特征列
	for i in range(numFeatures):
		featList = [example[i] for example in dataSet]  # 拿到第i列特征的所有值
		uniqueVals = set(featList) #去重
		newEntropy = 0.0

		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet) / float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)

		infoGain = baseEntropy - newEntropy
		if(infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i

	return bestFeature



'''
测试方法
'''
def test():
	dataSet = [[1, 1, 'yes'],
				[1, 1, 'yes'],
				[1, 1, 'maybe'],
				[0, 1, 'no'],
				[0, 1, 'maybe'],
				[1, 0, 'no'],
				[1, 0, 'no']]
	labels = ['no surfacing', 'flippers']

	shannonEnt = calcShannonEnt(dataSet)
	# print shannonEnt

	# a = splitDataSet(dataSet, 0, 1)
	# b = splitDataSet(dataSet, 0, 0)
	# print a
	# print b

	print chooseBestFeatureToSplit(dataSet)

if __name__ == '__main__':
	test()
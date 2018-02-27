# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

'''
这是一个使用matplotlib绘制的简单使用
'''


decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
	createPlot.ax1.annotate(nodeTxt, xy=parentPt, 
		xycoords='axes fraction', xytext=centerPt,
		textcoords='axes fraction', va="center",
		ha="center", bbox=nodeType, arrowprops=arrow_args)

def createPlotA():
	fig = plt.figure(1, facecolor='white')
	fig.clf()
	createPlot.ax1 = plt.subplot(111, frameon=False)
	plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode) 
	plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode) 

	plt.show()


'''
获取一个树结构的所有叶节点数量
'''
def getNumLeafs(myTree):
	if(myTree == None):
		return 0

	if type(myTree).__name__ != 'dict':
		return 1

	leafNums = 0
	for key in myTree.keys():
		leafNums += getNumLeafs(myTree[key])

	return leafNums

'''
获取一个树结构的深度
'''
def getTreeDepth(myTree):
	maxDepth = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]

	for key in secondDict.keys():
		if type(secondDict[key]).__name__ != 'dict':
			thisDepth = 1
		else:
			thisDepth = 1 + getTreeDepth(secondDict[key])

		if thisDepth > maxDepth:
			maxDepth = thisDepth

	return maxDepth


def plotMidText(cntrPt, parentPt, txtString):
	xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
	yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
	createPlot.ax1.text(xMid, yMid, txtString);

def plotTree(myTree, parentPt, nodeTxt):
	numLeafs = getNumLeafs(myTree)
	depth = getTreeDepth(myTree)

	firstStr = myTree.keys()[0]
	cntrpt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)

	plotMidText(cntrpt, parentPt, nodeTxt)
	plotNode(firstStr, cntrpt, parentPt, decisionNode)

	secondDict = myTree[firstStr]

	plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			plotTree(secondDict[key], cntrpt, str(key))
		else:
			plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
			plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrpt, leafNode)
			plotMidText((plotTree.xOff, plotTree.yOff), cntrpt, str(key))

	plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD



def createPlot(inTree):
	fig = plt.figure(1, facecolor='white')
	fig.clf()
	axprops = dict(xticks=[], yticks=[])
	createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)

	plotTree.totalW = float(getNumLeafs(inTree))
	plotTree.totalD = float(getTreeDepth(inTree))

	plotTree.xOff = -0.5/plotTree.totalW
	plotTree.yOff = 1.0

	plotTree(inTree, (0.5, 1.0), '')
	plt.show()



if __name__ == '__main__':
	testDict = {'flippers': {0: 'no', 1: {'no surfacing': {0: 'maybe', 1: 'yes'}}}}

	createPlot(testDict)
	# print getTreeDepth(testDict)





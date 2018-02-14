#-*- coding: UTF-8 -*-
import db
import model
import datetime
import config
def GetArticleTypeList():
	result = []
	dbResult = db.GetDataList("ARTICLE_TYPE")
	dbResult.sort(key=lambda x:x[2], reverse=True) 
	typeOfAll = model.ArticleType(0, u"全部")
	result.append(typeOfAll)
	if dbResult:
		for row in dbResult:
			typeItem = model.ArticleType(row[0], row[1])
			result.append(typeItem)

	return result

# 获取全部文章列表
def GetArticleList():
	result = []
	dbResult = db.GetDataList("ARTICLE")
	dbResult.sort(key=lambda x:x[3], reverse=True)
	if dbResult:
		for row in dbResult:
			submitDate = row[3]
			now = datetime.datetime.now()
			timedesc = u''
			tempDay = (now - submitDate).days
			if tempDay > 180:
				timedesc = u"很久以前"
			elif tempDay > 30:
				monthnum = tempDay / 30
				timedesc = u"%d个月以前" % (monthnum)
			elif tempDay > 0:
				timedesc = u"%d天前" % (tempDay)
			else:
				tempSecond = (now - submitDate).seconds
				hournum = tempSecond / 3600

				if hournum > 0:
					timedesc = u"%d个小时前" % (hournum)
				else:
					minnum = tempSecond / 60
					timedesc = u"%d分钟前" % (minnum)
			articleItem = model.ArticleDesc(row[0], row[1], timedesc, row[5])
			result.append(articleItem)

	return result

def GetArticleCount():
	total = db.GetDateCount("ARTICLE")
	return total

# 根据文章类型id获取文章列表
def GetArticleListByType(typeId):
	result = []
	dbResult = db.GetArticleByType(typeId)
	dbResult.sort(key=lambda x:x[3], reverse=True)
	if dbResult:
		for row in dbResult:
			submitDate = row[3]
			now = datetime.datetime.now()
			timedesc = u''
			tempDay = (now - submitDate).days
			if tempDay > 180:
				timedesc = u"很久以前"
			elif tempDay > 30:
				monthnum = tempDay / 30
				timedesc = u"%d个月以前" % (monthnum)
			elif tempDay > 0:
				timedesc = u"%d天前" % (tempDay)
			else:
				tempSecond = (now - submitDate).seconds
				hournum = tempSecond / 3600

				if hournum > 0:
					timedesc = u"%d个小时前" % (hournum)
				else:
					minnum = tempSecond / 60
					timedesc = u"%d分钟前" % (minnum)
			articleItem = model.ArticleDesc(row[0], row[1], timedesc, row[5])
			result.append(articleItem)

	return result

#根据类型以及分页信息获取文章列表
def GetPagingArticleList(typeId, keyword, pageIndex):
	pageSize = config.ARTICLE_LIST_PAGESIZE
	startNum = (pageIndex - 1) * pageSize
	dbResult = db.GetPagingArticleList(typeId, keyword, startNum, pageSize)
	articleList = []
	totalNum = 0
	if dbResult:
		for row in dbResult:
			totalNum = row[7]
			submitDate = row[3]
			now = datetime.datetime.now()
			timedesc = u''
			tempDay = (now - submitDate).days
			if tempDay > 180:
				timedesc = u"很久以前"
			elif tempDay > 30:
				monthnum = tempDay / 30
				timedesc = u"%d个月以前" % (monthnum)
			elif tempDay > 0:
				timedesc = u"%d天前" % (tempDay)
			else:
				tempSecond = (now - submitDate).seconds
				hournum = tempSecond / 3600

				if hournum > 0:
					timedesc = u"%d个小时前" % (hournum)
				else:
					minnum = tempSecond / 60
					timedesc = u"%d分钟前" % (minnum)
			articleItem = model.ArticleDesc(row[0], row[1], timedesc, row[5])
			articleList.append(articleItem)

	pageNum = totalNum / config.ARTICLE_LIST_PAGESIZE + 1 if (totalNum % config.ARTICLE_LIST_PAGESIZE > 0) else 0
	result = model.PagingViewModel(pageIndex, pageNum, articleList)
	return result


# 获取列表页信息
def GetListViewModel():
	typeList = GetArticleTypeList()
	totalNum = GetArticleCount()

	pageNum = totalNum / config.ARTICLE_LIST_PAGESIZE + 1 if (totalNum % config.ARTICLE_LIST_PAGESIZE > 0) else 0
	#articleList = GetArticleList()
	#result = model.ListViewModel(typeList,articleList)
	result = model.ListViewModel(typeList, totalNum, pageNum)
	return result;


#根据文章id获取文章详情
def GetArticleDetail(id):
	dbResult = db.GetArticleByID(id)
	if dbResult:
		row = dbResult[0]
		result = model.ArticleDetail(row[0], row[1], row[3], row[2], row[7], row[4], row[5], row[6])
		return result

	return None

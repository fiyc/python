#-*- coding: UTF-8 -*-
#列表页文章类型
class ArticleType:
	TypeId = 0
	TypeName = ''

	def __init__(self,id,name):
		self.TypeId = id
		self.TypeName = name


#列表页文章标题栏
class ArticleDesc:
	ArticleId = 0
	Title = ''
	TimeDesc = ''
	ReadNum = 0

	def __init__(self,id,title,timeDesc,readNum):
		self.ArticleId = id
		self.Title = title
		self.TimeDesc = timeDesc
		self.ReadNum = readNum

#详情页信息
class ArticleDetail:
	ArticleId = 0
	Title = ''
	Time = ''
	Content = ''
	TypeName = ''
	TypeId = ''
	ReadNum = 0
	EditType = 0

	def __init__(self, articleid, title, time, content, typename, typeid, readNum, editType):
		self.ArticleId = articleid
		self.Title = title
		self.Time = time
		self.Content = content
		self.TypeName = typename
		self.TypeId = typeid
		self.ReadNum = readNum
		self.EditType = editType


		
#列表页总信息
class ListViewModel:
	TypeList = []
	#ArticleList = []
	TotalNum = 0
	PageNum = 0

	#def __init__(self,typelist,articlelist):
	def __init__(self,typelist, totalNum, pageNum):
		self.TypeList = typelist
		self.TotalNum = totalNum
		self.PageNum = pageNum
		#self.ArticleList = articlelist


class PagingViewModel:
	TotalPageNum = 0
	PageIndex = 1
	ArticleList = []

	def __init__(self, pageIndex, totalPageNum, articlelist):
		self.PageIndex = pageIndex
		self.ArticleList = articlelist
		self.TotalPageNum = totalPageNum
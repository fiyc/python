import mysql.connector

def BeginConn():
	try:
		config = {
			'user' : 'yif',
			'password' : 'msn290850640',
			'host' : '127.0.0.1',
			'port' : '3306',
			'database' : 'blog'
		}
		conn = mysql.connector.connect(**config)
		return conn
	except Exception as e:
		return None

def GetDataList(tableName):
	conn = BeginConn()
	cur = conn.cursor()
	sql = "select * from %s" % (tableName)
	cur.execute(sql)
	result = cur.fetchall()

	cur.close()
	conn.close()

	return result

def GetDateCount(tableName):
	conn = BeginConn()
	cur = conn.cursor()
	sql = "select count(ID) from %s" % (tableName)
	cur.execute(sql)
	result = cur.fetchall()

	cur.close()
	conn.close()

	return int(result[0][0])

def GetArticleByID(id):
	conn = BeginConn()
	cur = conn.cursor()
	sql = "update ARTICLE SET READNUM = READNUM + 1 WHERE ID=%d" % (id)
	cur.execute(sql)
	sql = "select A.*, AT.Name from ARTICLE A inner join ARTICLE_TYPE AT on AT.ID = A.TYPE where A.ID=%d" % (id)
	cur.execute(sql)
	result = cur.fetchall()

	cur.close()
	conn.close()

	return result 

def GetArticleByType(type):
	conn = BeginConn()
	cur = conn.cursor()
	sql = ""
	if type == 0:
		sql = "select * from ARTICLE"
	else:
		sql = "select * from ARTICLE where TYPE=%d" % (type)
	cur.execute(sql)
	result = cur.fetchall()

	cur.close()
	conn.close()

	return result 

def GetPagingArticleList(type, keyword, startNum, pageSize):
	conn = BeginConn()
	cur = conn.cursor()

	sql = ""
	filterStr = ""
	if type != 0 or (keyword != None and keyword != ""):
		filterStr = "where 1=1"
		if type != 0:
			filterStr =  filterStr + " and TYPE=%d" % (type)
		if keyword != None and keyword != "":
			filterStr = filterStr + " and TITLE like '%%%%%s%%%%'" % (keyword)

	coutSql = ", (SELECT COUNT(1) FROM ARTICLE %s ) AS TotalNum" % (filterStr)	
	sql = "SELECT * %s FROM ARTICLE %s ORDER BY CREATE_TIME DESC LIMIT %d, %d" % ( coutSql, filterStr, startNum, pageSize)

	cur.execute(sql)
	result = cur.fetchall()

	cur.close()
	conn.close()

	return result
import os, sys
import mysql.connector

dir = "/home/yif/blog"
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

def GetContainFilePath(floderPath):
	paths = {}
	list = os.listdir(floderPath)

	for line in list:
		filepath = os.path.join(floderPath,line)
		if os.path.isdir(filepath):
			continue

		#paths.append(filepath)
		paths[line] = filepath


	return paths

def CommitFileContent(fileName, filePath):
	file_object = open(filePath)
	try:
		content = file_object.read()
		fileName = fileName.split('.')[0]
		articleInfo = fileName.split('_')
		sql = ""
		if len(articleInfo) == 3:
			articleTitle = articleInfo[0]
			articleType = articleInfo[1]
			articleEditType = articleInfo[2]
			sql = "insert into ARTICLE (TITLE, CONTENT, CREATE_TIME, TYPE, EDITTYPE) values ('%s', '%s', now(), %s, %s)" % (articleTitle, content, articleType, articleEditType)
		elif len(articleInfo) == 1:
			articleId =  articleInfo[0]
			sql = "update ARTICLE set CONTENT = '%s' where ID = %s" % (content, articleId)



		conn = BeginConn()
		cur = conn.cursor()
		cur.execute(sql)

		cur.close()
		conn.close()


	finally:
		file_object.close()

	os.remove(filePath)



fileDict = GetContainFilePath(dir)
for item in fileDict.keys():
	filePath = fileDict[item]
	CommitFileContent(item, filePath)



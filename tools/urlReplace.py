# -*- coding: utf-8 -*-
import os
import sqlite3
import re
import yifLibrary

allFilePath = []
connPath = 'D:\\MyConfiguration\\cyf30856\\Desktop\\test.db'
targetHome = "D:\\UbuntuShare\\jqNew"
def SaveFilePath():
	targetPath = ''
	sourcePath = 'D:\\UbuntuShare\\jq\\www.jquery123.com'

	conn = GetConn(connPath)
	InitCurrentFloderPath(sourcePath, conn)
	conn.close()



	print(len(allFilePath))

def InitCurrentFloderPath(path, conn):
	if(os.path.exists(path)):
		for dirpath, dirnames, filenames in os.walk(path):
			for filename in filenames:
				fullpath=os.path.join(dirpath, filename)
				if(os.path.isdir(fullpath)):
					InitCurrentFloderPath(fullpath, conn)

				elif(os.path.isfile(fullpath)):
					allFilePath.append(fullpath)
					sql  = "insert into docFileInfo values(null, '%s', %d)" % (fullpath, 0)
					ExecuteSql(conn, sql)

def GetConn(path):
	if(os.path.exists(path) and os.path.isfile(path)):
		return sqlite3.connect(path)
	else:
		print("useless path connection!")
		return None

def ExecuteSql(conn, sql):
	try:
		print(sql)
		cu = conn.cursor()
		cu.execute(sql)
		conn.commit()
		cu.close()
	except Exception as e:
		print(e)

def ReplaceUrl(content):
	urls = re.findall('<a href="(.*?)"', str(content))
	urls = list(set(urls))
	for each in urls:
		if(each.startswith("http")):
			continue

		strinfo = re.compile('<a href="'+ each +'"')
		content = strinfo.sub('<a href="'+ each +'index.html"',content)
		# content = content.replace(each, each + "index.html")
		
	return content

def OperateFile():
	conn = GetConn(connPath)

	cu = conn.cursor()
	sql = "select filepath from docFileInfo"
	cu.execute(sql)
	result = cu.fetchall()
	conn.close()
	if(len(result) > 0):
		for item in result:
			currentPath = str(item[0])	
			targetPath = currentPath.replace('\\','\\\\').replace('D:\\UbuntuShare\\jq\\', targetHome)
			targetPath = targetPath.replace('jq', 'jqN')

			currentContent = yifLibrary.IOHelper.GetFileContent(currentPath)
			targetContent = ReplaceUrl(currentContent)
			home = os.path.split(targetPath)[0]
			filename = os.path.split(targetPath)[1]
			yifLibrary.IOHelper.MakeDir(home)
			yifLibrary.IOHelper.SaveFile(targetPath, targetContent, 'wb')



# Main()
# conent = yifLibrary.IOHelper.GetFileContent("D:\\UbuntuShare\\jq\\www.jquery123.com\\index.html")
# c = ReplaceUrl(conent)
OperateFile()









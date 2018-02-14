import sys
import os

def SaveFile(filepath, content, editModel):
	fs = open(filepath, editModel)
	fs.write(content)
	fs.close()




def GetFileContent(filepath):
	if(os.path.exists(filepath) == False or os.path.isfile(filepath) == False):
		return ""

	fs = open(filepath, 'r')
	return fs.read()


def MakeDir(path):
	if(os.path.isdir(path)):
		return
	os.makedirs(path)



import subprocess
from yifLibrary import IOHelper 


def Match(baseJsonValue, targetJsonValue, Tag, outputPath="output"):
	print(outputPath)
	if(outputPath == ''):
		print("nopath")
		return

	baseJsonPath = outputPath + "\\base.json"
	targetJsonPath = outputPath + "\\target.json"

	IOHelper.SaveFile(baseJsonPath, baseJsonValue, 'wb')
	IOHelper.SaveFile(targetJsonPath, targetJsonValue, 'wb')

	cmd = 'CompareRun.exe ' + Tag + ' ' + outputPath
	input(cmd)
	ps = subprocess.Popen(cmd, stdin=subprocess.PIPE, shell=True)



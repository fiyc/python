import zipfile
import rarfile

passwordCharacter = "abcdefghijklmnopqrstuvwxyz123456789-"


def GetPasswordKeys(ignoreCase=False):
	try:
		if ignoreCase == True:
			upperCharacter = passwordCharacter.upper()
			lowCharacter = passwordCharacter.lower()
			lowKeys = list(lowCharacter)
			upperKeys = list(upperCharacter)
			baseKeys = list(passwordCharacter)

			baseKeys.extend(lowKeys)
			baseKeys.extend(upperKeys)

			return list(set(baseKeys))
		else:
			return list(set(list(passwordCharacter)))

	except Exception as e:
		print(e) 
		return []


def CheckCPFilePassword(cpFile, password):
	try:
		password = str.encode(password)
		cpFile.extractall(pwd=password)
		return True
	except Exception as e:
		print(e)
		return False



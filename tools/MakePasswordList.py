import array
import zipfile
import rarfile


def checkPassword(zfile, password):
	try:
		zfile.extractall(pwd=password)
		print("success")
		return True
	except Exception as e:
		print(e)
		return False


path = "test.zip"
zfile = None
if path.endswith('.zip'):
	zfile = zipfile.ZipFile(path)
elif path.endswith('.rar'):
	zfile = rarfile.RarFile(path)
passwordLength = 1

# checkPassword(zfile, str.encode("a"))
# zfile.close()

key = "abcdefghijklmnopqrstuvwxyz1234567890-"
upperKey = key.upper()
keys = list(key)
upperKeys = list(upperKey)
keys.extend(upperKeys)

keys = list(set(keys))

keyLength = len(keys)

passIndex = []
for index in range(0, passwordLength):
	passIndex.append(0)

print(keys)
try:
	loop = True
	while loop:
		password = "" 
		for item in passIndex:
			password = password + str(keys[item])

		
		print("try password: " + password)
		if checkPassword(zfile, str.encode(password)):
			print ("find the password: " +  password)
			loop = False
			break

		passIndex.reverse()

		for index in range(0, len(passIndex)):
			indexValue = passIndex[index]
			if indexValue < keyLength - 1:
				passIndex[index] = indexValue + 1
				break;
			else:
				passIndex[index] = 0;
				if index == len(passIndex) - 1:
					loop = False

		passIndex.reverse()

	zfile.close()
	print("finish")
except Exception as e:
	print(e)

input()


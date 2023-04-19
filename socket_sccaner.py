from math import trunc
import socket
import subprocess
import sys 
import datetime 
import datetime
from unittest import result


subprocess.call("clear")


remoteserver = input("please type your Ip adress fo scaning")
remoteserverip = socket.gethostbyname(remoteserver)

print("-Capo-"*30)
print("please wait we are scaning : ", remoteserverip)
print("-Capo-"*30)

time1 = datetime.now()

try:
    for port in range (1,50):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Result = sock.connect_ex((remoteserverip,port))
        if result == 0:
            print("port {} :            open".format(port))

except KeyboardInterrupt:
    print("thanks for usinل, bye")
    sys.exit()
except socket.gaierror:
    print("our syste cannot connect to the host")
    sys.exit()
except socket.error:
    print("we got ERROR")
    sys.exit()


time2 = datetime.now()


time3 = time2 - time1 

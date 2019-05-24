# import os
# import re
# import time
# import sys
# from threading import Thread

# class TestePing(Thread):
#    def __init__ (self,ip):
#       Thread.__init__(self)
#       self.ip = ip
#       self.status = -1
#    def run(self):
#       pingaling = os.popen("ping -q -c2 "+self.ip,"r")
#       while 1:
#         line = pingaling.readline()
#         if not line: break
#         igot = re.findall(TestePing.lifeline,line)
#         if igot:
#            self.status = int(igot[0])

# TestePing.lifeline = re.compile(r"(\d) received")
# report = ("Sem resposta","Resposta parcial","Ativo")

# print (time.ctime())

# pinglist = []

# for host in range(60,70):
#    ip = "127.0.0."+str(host)
#    current = TestePing(ip)
#    pinglist.append(current)
#    current.start()

# for pingle in pinglist:
#    pingle.join()
#    print ("Server <",pingle.ip,"> -",report[pingle.status])

# print (time.ctime())
import time
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list):
    def append(self,par,kyda):
        super().append(par)
        Loggable.log(self,par)
        kyda.append(par)
        
        
a=list()
opr=LoggableList()
opr.append(7,a)
print(a)


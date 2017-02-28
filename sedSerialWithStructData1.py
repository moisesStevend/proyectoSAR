from struct import *
import serial
import time
import sys 

def sendData(s,data):
    s.write(data)
    return s.read(size=1)

##########preescaler:###########
#------------------------------
# No | pres1 | pres0 |   modo  |
#------------------------------
# 0  |   0   |   0   |  10     |
# 1  |   0   |   1   |  100    |
# 2  |   1   |   0   |  1000   | 
# 3  |   1   |   1   |  10000  |
#------------------------------
##########freq=[0-7]############
# freq_max=7
# freq_min=0
################################

def configPWM(hab=0, presNo=0, freq=0, dir=0, startStop=0):
    paquete=(startStop<<7)|(dir<<6)|(freq<<3)|(presNo<<1)|hab
    return pack('b',paquete)

def getStep(s):
    return s.read(size=4)

if __name__=="__main__":
    try:
        try:
            ser=serial.Serial('/dev/ttyACM0',9600)
        except:
            print 'No hay puerto serial disponible, verifique la conexion'
            sys.exit()

        #data=pack('bbbb',ord('a'),ord('a'),ord('b'),ord('b'))
        data=configPWM(hab=1,presNo=2, freq=5, dir=0, startStop=0)
        print len(data)
        print sendData(ser,data)
    except KeyboardInterrupt:
        print "adios!"
        ser.close()
        sys.exit()

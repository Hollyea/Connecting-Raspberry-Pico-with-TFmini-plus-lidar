from machine import UART, Pin
import time

uart1 = UART(1, baudrate=115200, tx=Pin(8), rx=Pin(9))    #Define receiving interface of Lidar 
uart0 = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))    #Define printing interface

def getLidarData(UART1,UART0):
    temp = bytes()
    if UART1.any() > 0:
        temp += UART1.read(9)
        if temp[0] == 0x59 and temp[1] == 0x59 :
            distance   = temp[2] + temp[3] * 256             #Get distance value  
            strength    = temp[4] + temp[5] * 256            #Get Strength value  
            temperature= (temp[6] + temp[7]* 256)/8-256      #Get IC temperature value  
            #UART0.write(bytes(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8]))
            UART0.write(temp)
            #UART0.write('\r\n')
            print("distance =%5dcm,strength = %5d,temperature = %5d℃"%(distance,strength,temperature))
while True:
    getLidarData(uart1,uart0)


# -*- coding: utf-8 -*-
import serial


#打开串口
serialPort="/dev/ttyS0"   #串口
baudRate=115200      #波特率
ser=serial.Serial(serialPort,baudRate,bytesize=8, parity='N', stopbits=1,timeout=60)
print("参数设置：串口=%s ，波特率=%d"%(serialPort,baudRate))

print(ser.isOpen())

#收发数据

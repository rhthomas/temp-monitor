#!/usr/bin/python3
# file    : temp.py
# author  : rt8g15
# created : 2016-12-01

from datetime import datetime
import Adafruit_BMP.BMP085 as BMP085
import csv

sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)

# collect data
now = datetime.now().strftime('%Y%m%d%H:%M')
time = now[-5::] # time is the last 5 symbols
temp = sensor.read_temperature()

# data to be sent to csv
data = [time,temp]

# open csv or create if !exist
with open('/home/pi/temp-monitor/data/'+now[:-5]+'.csv','a') as file:
    a = csv.writer(file, delimiter=',')
    a.writerow(data)

#!/usr/bin/python3
# file    : plot.py
# author  : rt8g15
# created : 2016-12-01

# needed since pi-0 has no frontend
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from csv import reader
from datetime import datetime

# name for files
name = datetime.now().strftime('%Y%m%d')

with open('/home/pi/temp-monitor/data/'+name+'.csv','r') as f:
  data = list(reader(f))

time = [data[i][0] for i in range(len(data))]
temp = [data[i][1] for i in range(len(data))]
dateObj = []

# convert string to datetime object
for t in time:
  dateObj.append(datetime.strptime(t,'%H:%M'))

# plot data
plt.plot(dateObj,temp)

# axis styling
ax = plt.gca()
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))
ax.axes.set_ylim([0,25])
plt.title(name)
plt.xlabel('Time (hh:mm)')
plt.ylabel('Temperature (°C)')

# save image
plt.savefig('/home/pi/temp-monitor/images/'+name+'.png')
plt.savefig('/home/pi/temp-monitor/images/'+name+'.eps')

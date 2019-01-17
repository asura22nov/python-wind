'''
Wind turbine efficiency or power coefficient.
The available power in a stream of wind of the same cross-sectional area as the wind turbine can easily be shown to be

Potential power

P= (1/2)*density*velocity^3*area

density = 1.225 kg/m^3
Diameter = 90 m
Area = 2025*pi = 6362 m^2

If the wind speed U is in metres per second, the density ρ is in kilograms per
cubic metre and the rotor diameter d is in metres then the available power
is in watts. 
'''

######################################################################
import csv
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

######################################################################
#
#Read wind data
#
######################################################################

x,y = [],[]
csv_reader = csv.reader(open('E:\\anand\\python\\winddata.01112015_1.CSV'))
for line in csv_reader:
   x.append(float(line[1]))  #windspeed
   y.append(dt.datetime.strptime(line[0],'%m/%d/%Y %H:%M')) #date and time in 15 min slot


fig = plt.figure()
ax1 = fig.add_subplot(221)
#plt.axis([0.0,25.0,0.0,24.0])
ax1.plot(y,x,'ro-')
ax1.set_ylim([0, 15])

ax1.fmt_xdata = DateFormatter('%H:%M')
fig.autofmt_xdate()
ax1.xaxis.set_major_formatter(DateFormatter('%H:%M'))
plt.title('wind speed data')
plt.ylabel('wind speed')
plt.xlabel('hours')
plt.grid(True)

######################################################################
#
#Read power curve
#
######################################################################

p= 0.5*1.225*6362*(np.array(x))**3

ax2 = fig.add_subplot(222)
#plt.axis([0.0,25.0,0.0,24.0])
ax2.plot(y,p,'bo-')
ax2.fmt_xdata = DateFormatter('%H:%M')
##fig.autofmt_xdate()
##ax2.xaxis.set_major_formatter(DateFormatter('%H:%M'))
plt.xlabel('hours')
plt.ylabel('power in KW')
plt.title('Wind power curve for 2MW')
plt.grid(True)

######################################################################
#
#Read grid committed power
#
######################################################################
a,b = [],[]
csv_reader = csv.reader(open('E:\\anand\\python\\grid_schedule.CSV'))
for line in csv_reader:
   a.append(float(line[1]))  #power committed in KW
   b.append(dt.datetime.strptime(line[0],'%H:%M')) #date and time in 15 min slot

ax3= fig.add_subplot(223)
ax3.plot(b,a,'go-')
##ax3.fmt_xdata = DateFormatter('%H:%M')
##fig.autofmt_xdate()
##ax3.xaxis.set_major_formatter(DateFormatter('%H:%M'))
plt.xlabel('hours')
plt.ylabel('power in KW')
plt.title('Grid power committed')
plt.grid(True)
######################################################################
#
######################################################################
ax4 = fig.add_subplot(224)
ax4.plot(y,p,'bo-')
ax4.plot(b,a,'go-')
ax4.fmt_xdata = DateFormatter('%H:%M')
ax4.xaxis.set_major_formatter(DateFormatter('%H:%M'))
plt.grid(True)
plt.show()

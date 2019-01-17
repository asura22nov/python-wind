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


import csv
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

x,y = [],[]
csv_reader = csv.reader(open('E:\\anand\\python\\powercurve.01112015_1.CSV'))
for line in csv_reader:
   y.append(float(line[1]))
   x.append(float(line[0]))
   #y.append(dt.datetime.strptime(line[0],'%m/%d/%Y %H:%M'))

p= 0.5*1.225*6362*(np.array(x))**3

#print(p)
fig = plt.figure()
ax = fig.add_subplot(111)
#plt.axis([0.0,25.0,0.0,24.0])
ax.plot(x,y,'bo-')
plt.xlabel('wind speed')
plt.ylabel('power in KW')
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.title('Wind power curve for 2MW')
plt.show()

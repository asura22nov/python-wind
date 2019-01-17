import csv
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange

a,b = [],[]
csv_reader = csv.reader(open('E:\\anand\\python\\grid_schedule.CSV'))
for line in csv_reader:
   a.append(float(line[1]))  #power committed in KW
   b.append(dt.datetime.strptime(line[0],'%H:%M')) #date and time in 15 min slot

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(b,a,'go-')


###plt.axis([0.0,25.0,0.0,24.0])
##ax1.plot(y,x,'ro-')
##
##print(dt.datetime.strptime(line[0],'%d/%m/%Y %H:%M'))
##fig = plt.figure()
##ax = fig.add_subplot(111)
###plt.axis([0.0,25.0,0.0,24.0])
##ax.plot(y,x,'ro-')
##
###ax.set_xlim([dt.datetime.strptime(line[0],'%m/%d/%Y %H:%M'),dt.datetime.strptime(line[0],'%m/%d/%Y %H:%M')])
##ax.set_ylim([0, 15])
##
ax.fmt_xdata = DateFormatter('%H:%M')
fig.autofmt_xdate()
ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
##plt.title('wind speed data')
##plt.ylabel('wind speed')
##plt.xlabel('hours')
##
plt.show()


'''
0,43:48.1
1,45:13.1
2,47:50.1
3,55:02.3

import csv
with open('E:\\anand\\python\\AWS20151101-42674.9399503009.CSV') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row)
'''

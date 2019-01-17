import csv
import datetime as dt
import matplotlib.pyplot as plt

x,y = [],[]
csv_reader = csv.reader(open('E:\\anand\\python\\data_2.CSV'))


for line in csv_reader:
    print(dt.datetime.strptime(line[0],'%d/%m/%Y %H:%M'))
'''
    #x.append(int(line[0]))
    #y.append(dt.datetime.strptime(line[1],'%M:%S.%f'))
    


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(y,x,'o-')
fig.autofmt_xdate()

plt.show()

Assuming data.csv file containing data like these:

0,43:48.1
1,45:13.1
2,47:50.1
3,55:02.3
1/11/2015 0:00,22.7,94,968.2,0,359
'''

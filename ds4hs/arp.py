#WK3: Groups and Apply

from datascience import *
import numpy as np

arp = Table.read_table('/home/abcaslow/data8/arpSearchResults.csv')
cam = Table.read_table('/home/abcaslow/data8/cam-master.csv')

#nba1.show(5)    displays no table. Instead it displays this:  <IPython.core.display.HTML object>
# may be nba1.show(5) only works in jupyter notebooks
#I don't know what the following command does: nba_10 = nba1.take(np.arange(10))
arp1 = arp.take(np.arange(10))
cam_q=cam.select('Interface','Registration')
#nba = nba1.relabeled("2015-2016 SALARY", 'SALARY')
#teams_and_money = nba.select('TEAM', 'SALARY')
#teams_and_money.group('TEAM', sum)
#nba.group('POSITION')
#What was the average salary of the players at each of the five positions?
#positions_and_money = nba.select('POSITION', 'SALARY')
#positions_and_money.group('POSITION', np.mean)
#nba.group('POSITION', np.mean) ## RUN THIS CELL
#EXTRA CREDIT: Find the highest player salary for each team, then sort the teams in order of highest player salaries.
#Hint: think about which columns you need, what you would group by, and finally what you would sort by.
#teams_and_money = nba.select('TEAM', 'SALARY')
#teams_and_money.group('TEAM', max).sort('SALARY max', descending = True)
#=================================
cam_q.where("Registration", are.containing("ell"))
cam_q.where("Interface", are.containing("Eth1/1"))
cam_q.where("Interface", are.containing("Eth1/11"))
cam.group('Interface')
cam.group('Registration')
cam.group('Registration', max)
#cam.group('Registration', count) #Error count does not work
cam.group('Registration', min)
cam_q
cam_q.group('Registration', min)
cam_q.group('Registration', max)
cam_q.group('Registration', sum)
cam_q.group('Registration', np.mean)
cam_q.group('Registration')
cam_q.group('Registration').sort
#cam_q.group('Registration').count.sort # .count.sort does not work
cam_q.group('Registration').show(10)

#The following is very useful
# The following command adds the "count" column from te group operation.
#It is all saved to the new name 'y'y.
y=cam_q.group('Registration')
#The following command  sorts on the new "count" column.
y.sort('count', descending=True)


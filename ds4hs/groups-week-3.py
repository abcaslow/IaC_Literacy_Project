#WK3: Groups and Apply

from datascience import *
import numpy as np

#Groups
#The datascience "group" command is like the python "set" command.
#The group command operates on data in rows of a datascience table
# This entire 'groups' notebook is derived from the following data8 lesson:
#https://www.inferentialthinking.com/chapters/08/2/Classifying_by_One_Variable.html
#This chapter in Inferential Thinking is awesome!!!!
#Cut and paste the examples from this Data8 module to master groups.

#https://www.inferentialthinking.com/chapters/08/3/Cross-Classifying_by_More_than_One_Variable.html
#This is a great chapter on grouping by multiple variables and the amazing PIVOT method


cones = Table().with_columns(
    'Flavor', make_array('strawberry', 'chocolate', 'chocolate', 'strawberry', 'chocolate'),
    'Price', make_array(3.55, 4.75, 6.55, 5.25, 5.25)
)
cones # RUN THIS CELL
cones.group('Flavor') # RUN THIS CELL
cones.group('Flavor', sum)
cones.group('Flavor', min)

nba1 = Table.read_table('/home/abcaslow/BUDS-su20/Week_3/Group/nba_salaries.csv')
#nba1.show(5)    displays no table. Instead it displays this:  <IPython.core.display.HTML object>
# may be nba1.show(5) only works in jupyter notebooks
#I don't know what the following command does: nba_10 = nba1.take(np.arange(10))
nba_10 = nba1.take(np.arange(10))

nba = nba1.relabeled("2015-2016 SALARY", 'SALARY')
teams_and_money = nba.select('TEAM', 'SALARY')
teams_and_money.group('TEAM', sum)
nba.group('POSITION')
#What was the average salary of the players at each of the five positions?
positions_and_money = nba.select('POSITION', 'SALARY')
positions_and_money.group('POSITION', np.mean)
nba.group('POSITION', np.mean) ## RUN THIS CELL
#EXTRA CREDIT: Find the highest player salary for each team, then sort the teams in order of highest player salaries.
#Hint: think about which columns you need, what you would group by, and finally what you would sort by.
teams_and_money = nba.select('TEAM', 'SALARY')
teams_and_money.group('TEAM', max).sort('SALARY max', descending = True)


#www.github.com/data-8

from datascience import *
import numpy as np
import matplotlib

#load your python modules listed above
#load your data. Use %pwd, %ls, %cd to move your LINUX FS pwd to where you want it to be to load your csv file
#isolate your initial data analysis to just 1-3 columns with a select or drop command
# grab specific data with the "where" command and sort the data.
# graph the data


confirmed_cases = Table().read_table("~/BUDS-su20/Project_1/data/covid_by_county.csv").drop(3)
#confirmed_cases.show(10)   <= What does this command do?
confirmed_cases_clean = confirmed_cases.relabel(make_array("4/1/2020", "5/1/2020", "6/1/2020"), make_array("April", "May", "June"))
confirmed_cases_clean
sorted_cases = confirmed_cases_clean.sort("April", descending = True)
#sorted_cases
top_ten = sorted_cases.take(np.arange(10))
cdir=[varname for varname in dir() if not varname.startswith('_')]
#top_ten
print('top_ten.barh("County", "April")')
print('top_ten.bar("County", "April")')
print('top_ten.hist("April")')
#ca_cases = sorted_cases.where("State", are.equal_to("California"))
#ca_cases = sorted_cases.where("State", are.equal_to("Maryland"))
print('va_cases = sorted_cases.where("State", are.equal_to("Virginia"))')
print('va_top10=va_cases.take(np.arange(10))')
print('va_top10.barh("County", "April")')
#print(va_top10.bar("County", "April"))
print('county_cases = confirmed_cases.where("County", are.equal_to("Fairfax")).drop(2)')
print('%matplotlib')

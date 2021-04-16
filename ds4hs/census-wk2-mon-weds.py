#Week 2/Monday: CENSUS Lab - A very short lab
from datascience import *
import numpy as np
#path_data = '../../../../data/'
#np.set_printoptions(threshold=50)

cdir=[varname for varname in dir() if not varname.startswith('_')]

# As of Jan 2017, this census file is online here: 
data = 'http://www2.census.gov/programs-surveys/popest/datasets/2010-2015/national/asrh/nc-est2015-agesex-res.csv'

# A local copy can be accessed here in case census.gov moves the file:
# data = path_data + 'nc-est2015-agesex-res.csv'

full_census_table = Table.read_table(data)
full_census_table

#================================================
#WK2/Tuesday: Lists & Acquiring and Cleaning Data: with CENSUS Data Again
#Just like WK2/Monday, it is a short lab.

partial_census_table = full_census_table.select('SEX', 'AGE', 'POPESTIMATE2010', 'POPESTIMATE2014')
us_pop_relabel = partial_census_table.relabeled('POPESTIMATE2010', '2010')

us_pop = us_pop_relabel.relabel("POPESTIMATE2014", "2014")

#=================================================
#WK2/WEDS: Row Filtering with where and take
#John Denero - Data 8X, Census: Males and Females. 
#https://www.youtube.com/watch?v=SAJavz58uHk&feature=youtu.be
#Data 8 Spring 2020 - Lab 02. http://data8.org/sp20/

males_pop = us_pop.where('SEX', are.equal_to(1))
females_pop = us_pop.where('SEX', are.equal_to(2))
ten_yr_males = males_pop.where("AGE", 10)
us_pop.sort("AGE", descending = True)
pop_by_age = us_pop.where("AGE", are.below(999)).sort("AGE", descending= True)
pop_by_age.barh("AGE", "2014")
both_sexes = pop_by_age.where("SEX", are.above(0))
both_sexes = pop_by_age.where("SEX", are.between(1, 3))

###Working with TAKE
#http://data8.org/datascience/_autosummary/datascience.tables.Table.take.html
#Return a new Table with selected rows taken by index.

us_pop_2014 = us_pop.where("SEX", are.above(0)).where("AGE", are.below(999)).drop("2010")
us_pop_2014_sorted = us_pop_2014.sort("AGE", descending = True)
us_pop_2014_sorted.take(0)
seniors_2014 = us_pop_2014_sorted.take(np.arange(0,6)) ## YOUR CODE HERE
seniors_2014 = us_pop_2014_sorted.where("AGE", are.between(98, 101))

#----------------------------------------------------
#Predicate       Example Result
#are.equal_to    are.equal_to(50)        Find rows with values equal to 50
#are.equal_to    are.equal_to("hello")   Find rows with values equal to "hello"
#are.not_equal_to        are.not_equal_to(50)    Find rows with values not equal to 50
#are.above       are.above(50)   Find rows with values above (and not equal to) 50
#are.above_or_equal_to   are.above_or_equal_to(50)       Find rows with values above 50 or equal to 50
#are.below       are.below(50)   Find rows with values below 50
#are.between     are.between(2, 10)      Find rows with values above or equal to 2 and below 10
#are.containing  are.containing("i")     Find rows with string values that contain the letter i.
#-----------------------------------------------------

#THIS CODE ADDS THE STRING VERSION OF SEX IN A NEW COLUMN
#LOOK AT THE NEW FAR RIGHT COLUMN

fem_str = females_pop.with_column("SEX (str)" ,"female")
male_str = males_pop.with_column("SEX (str)" , "male")
str_sex = fem_str.with_rows(male_str.rows).sort('AGE', descending=True)

str_sex.where("SEX (str)", are.equal_to("female"))

## OPTION 2: uses the default argument of are.equal_to(...) 
## to find rows where "SEX (str)" is equal to "female"
str_sex.where("SEX (str)", "female")

str_sex.where("SEX (str)", are.containing("fe"))

# From YouTube video by John Denero

vus_pop_2014=us_pop.drop('2010').where('AGE', are.below(999)).where('SEX', are.above(0))
sum(vus_pop_2014.column('2014'))
vmales=vus_pop_2014.where('SEX', 1).column('2014') #makes and array
# The following works but the next line which builds on it does not because of something after 'relabel'
# In the video, there are two data columns. I only have one in us_pop after the 'drop('2010') 5 lines above. 
vby_sex=vus_pop_2014.where('SEX', 2).drop('SEX')
#vby_sex=vus_pop_2014.where('SEX', 2).drop('SEX').relabel('2015', 'Females').with_column('Males',vmales)
#vby_sex.set_format('Males', NumberFormatter)
#vby_sex.row(0).item('Males') /vby_sex.row(0).item('Females')
#vbysex.plot(0)

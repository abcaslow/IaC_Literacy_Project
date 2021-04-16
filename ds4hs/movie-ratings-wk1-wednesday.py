import numpy as np
from datascience import *
#/home/BruceCaslow/BUDS-su20/Week_1/data
ratings = Table.read_table("/home/abcaslow/BUDS-su20/Week_1/data/imdb_ratings.csv")
print('ratings.num_columns')
print('ratings.num_rows')
print('ratings.select("Votes","Title")')
print('ratings.drop("Decade")')
print('ratings.show(20)')
print('ratings.sort("Year")')
print('ratings.sort("Year", descending=True)')


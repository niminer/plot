import csv
import pandas as pd
import numpy as np

from pyecharts import options as opts
from pyecharts.charts import Pie, Bar, Page
from Csv import CSVPlotter

my_c = CSVPlotter('older.csv')
index = (1,9)
cc = my_c.get1dcolumn(index)
index = (9,12)
ff = my_c.get2dcolumn(index)
# print(cc)
# print(ff)
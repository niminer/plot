import csv
import pandas as pd
import numpy as np

from pyecharts import options as opts
from pyecharts.charts import Pie, Bar, Page
from pyecharts.charts import Bar
from Csv import CSVPlotter

my_c = CSVPlotter('older.csv')
index = (1,2,9,10,11,12)
cc = my_c.get1dcolumn(index)
index = (9,12)
ff = my_c.get2dcolumn(index)
# print(ff[3])

c = (
    Pie()
    .add("", [list(z) for z in zip(cc['住房情况'].keys(), cc['住房情况'].values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-住房情况"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_region.html")
)

bar = Bar()
bar.add_xaxis(sorted(ff[0]))
for i in range(len(ff[4])):
    bar.add_yaxis(ff[4][i], ff[1][i].tolist())
bar.set_global_opts(title_opts=opts.TitleOpts(title="自理情况和居住状况"))
bar.render()

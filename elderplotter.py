import csv
import pandas as pd
import numpy as np

from pyecharts import options as opts
from pyecharts.charts import Pie, Bar, Page
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
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-住房情况"),
                     legend_opts=opts.LegendOpts(type_="scroll",pos_right="20%",orient="horizontal"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    #.render("pie_region.html")
)

c2= (
    Pie()
    .add("", [list(z) for z in zip(cc['性别'].keys(), cc['性别'].values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-性别比例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    #.render("pie_region.html")
)

bar = Bar()
bar.add_xaxis(sorted(ff[0]))
for i in range(len(ff[4])):
    bar.add_yaxis(ff[4][i], ff[1][i].tolist())
bar.set_global_opts(title_opts=opts.TitleOpts(title="自理情况和居住状况"),
                    legend_opts=opts.LegendOpts(type_="scroll",pos_left="80%",orient="vertical"))
#bar.render()

page = Page()
page.add(
    bar, c,c2
)
page.render("page_simple_layout.html")

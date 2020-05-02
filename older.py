import csv
import numpy as np
from datetime import datetime

from pyecharts import options as opts
from pyecharts.charts import Pie, Bar, Page

filename = 'older.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)

    older = {}
    index = (1, 11)
    for i in range(len(index)):
        older[header[index[i]]] = {}
    for row in reader:
        for column in index:
            for item in row[column].split(','):
                if item not in older[header[column]].keys():
                    older[header[column]][item] = 1
                else:
                    older[header[column]][item] += 1

    # xs = {}
    # for i in older[header[11]].keys():
    #     x = i.split(',')
    #     for j in x:
    #         xs[j] = 0
    #
    # print(xs.keys())
    print(older)

    # region, sex, date, marry, edu = [], [], [], [], []
    # cnt_sex = []
    # cnt_region = []
    # cnt_marry = []
    # cnt_edu = []
    #
    # for row in reader:
    #     region.append(row[1])
    #     sex.append(row[2])
    #     date.append(row[5])
    #     marry.append(row[6])
    #     edu.append(row[8])
    # print(edu)
    #
    # cnt_sex_flag = ['男', '女']
    # for i in range(2):
    #     cnt_sex.append(sex.count(cnt_sex_flag[i]))
    #
    # cnt_region_flag =['农村','城市']
    # for i in range(2):
    #     cnt_region.append(region.count(cnt_region_flag[i]))
    #
    # cnt_date_flag = []
    # for i in range(2):
    #     cnt_region.append(region.count(cnt_region_flag[i]))
    #
    # cnt_marry_flag = ['未婚','已婚','丧偶','离婚','未说明的婚姻状况']
    # for i in range(5):
    #     cnt_marry.append(marry.count(cnt_marry_flag[i]))
    #
    # cnt_edu_flag = ['文盲（或半文盲）','小学','初中','高中/技校/中专','大学专科及以上','不详']
    # for i in range(6):
    #     cnt_edu.append(edu.count(cnt_edu_flag[i]))
    # print(cnt_edu)
    #
    #     # current_date = datetime.strptime(row[5], "%Y-%m-%d")
    #     # date.append(current_date)
    #     # edu.append(row[8])
    #
    # c = (
    #     Pie(init_opts=opts.InitOpts(height="500px", width="500px"))
    #         .add(
    #         "",
    #         # [("男",58),("女",42)],
    #         [list(z) for z in zip(region, cnt_region)],
    #         # center=["35%", "50%"],
    #     )
    #         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    #
    # )
    # c.render("pie_region.html")
    #
    # bar = (
    #     Bar(init_opts=opts.InitOpts(height="500px", width="500px"))
    #     .add_xaxis(cnt_edu_flag)
    #     .add_yaxis("文化程度", cnt_edu)
    #     .set_global_opts(title_opts=opts.TitleOpts(title="文化程度"))
    # )
    # bar.render()

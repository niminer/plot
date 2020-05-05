import csv
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
import numpy as np

health = ('', '健康', '患有大病（有证）', '患有1种老年慢性病', '患有2种老年慢性病', '患有3种及以上老年慢性病')
house = ('', '自有住房', '从市场租房', '住廉租住房或公共租赁住房', '住公有住房', '住军产房或宗教产房', '住直系亲属房', '其他')
income =(
'无',
'企业职工离退休金',
'机关、事业单位离退休金',
'部队人员离退休（役）金',
'城乡居民养老保险金',
'新型农村社会养老保险金',
'低保补助金',
'特困人员补助金',
'遗属补助金',
'计划生育特别扶助对象补助金',
'子女/抚养补贴',
'亲友资助',
'其他'
)
elder_type =('','无','离退休人员','残疾人员（有证）','城镇低保老人','农村低保老人','“三老”优抚对象（老复员军人、老伤残军人、老烈属）'
,'城镇特困人员'
,'农村特困人员'
,'城镇计划生育特别扶助对象'
,'农村计划生育特别扶助对象'
,'城市空巢老人'
,'农村留守老人')


filename = 'older.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)

    older = {}
    index = (9, 12)
    for i in range(len(index)):
        older[header[index[i]]] = []
    for row in reader:
        for column in index:
            # if row[column] not in older[header[column]].keys():
            older[header[column]].append(row[column])
        # else:
        #     older[header[column]][row[column]] += 1
    # print(older)

    od = pd.DataFrame(older)
    x = []  #x为自理情况分类
    # y1 = {}
    y2 = {}  #y2={"i",j.iloc[:, 0].size}
    z = []   #z为性别分类
    w = []  #w为性别和自理能力的组合情况
    # y = [[0,0],[0,0],[0,0],[0,0],[0,0]]
    for i, j in od.groupby([older[header[9]], older[header[12]]]):
        # print(i)
        # print(j.iloc[:, 0].size)
        # print(j)
        if i[1] not in x:
            x.append(i[1])
        # y1.setdefault(i[1], []).append(j.iloc[:, 0].size)
        y2[i] = j.iloc[:, 0].size

        if i[0] not in z:
            z.append(i[0])
    # print(y2)
    #y2 = list(y2)

    for x1 in x:
        for z1 in z:
            w.append((z1, x1))
            if (z1, x1) not in list(y2):
                #y2.insert(x.index(x1) * len(x) + z.index(z1), (z1, x1))
                y2[(z1, x1)] = 0

    idx = 0
    yy = np.zeros(len(z)*len(x), dtype=int)    #创建一个全0的数组，数组的长度是len(z)*len(x)
    for i in sorted(y2.keys()):   #sorted 排序
        yy[idx] = y2[i]
        idx += 1

    yy.resize((len(z), len(x)))  # 将yy转换成len(z)行 len(x)列的数组
    print(sorted(x))
    print(z)
    print(yy[0, :])
    print(yy[1, :])

# bar = (
#     Bar()
#         .add_xaxis(sorted(x))
#         .add_yaxis(z[0], yy[0].tolist())
#         .add_yaxis(z[1], yy[1].tolist())
#         .add_yaxis(z[2], yy[2].tolist())
#         .add_yaxis(z[3], yy[3].tolist())
#         .set_global_opts(title_opts=opts.TitleOpts(title="自理情况和健康状况"))
# )
# bar.render()

    bar = Bar()
    bar.add_xaxis(sorted(x))
    for i in range(len(z)):
        bar.add_yaxis(z[i], yy[i].tolist())
    bar.set_global_opts(title_opts=opts.TitleOpts(title="自理情况和居住状况"))
    bar.render()

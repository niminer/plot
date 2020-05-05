import csv
import pandas as pd
import numpy as np

class CSVPlotter():
    def __init__(self, filename):
        self.filename = filename

    def get1dcolumn(self, index):
        count_tmp = {}
        with open(self.filename) as f:
            reader = csv.reader(f)
            header = next(reader)
            for i in range(len(index)):
                count_tmp[header[index[i]]] = {}
            for row in reader:
                for column in index:
                    for item in row[column].split(','):
                        if item not in count_tmp[header[column]].keys():
                            count_tmp[header[column]][item] = 1
                        else:
                            count_tmp[header[column]][item] += 1
        return count_tmp


    def get2dcolumn(self, index):
        count_tmp2 = {}
        with open(self.filename) as f:
            reader = csv.reader(f)
            header = next(reader)
            for i in range(len(index)):
                count_tmp2[header[index[i]]] = []
            for row in reader:
                for column in index:
                    count_tmp2[header[column]].append(row[column])

        od = pd.DataFrame(count_tmp2)
        x = []  # x为自理情况分类
        y2 = {}  # y2={"i",j.iloc[:, 0].size}
        z = []  # z为性别分类
        w = []  # w为性别和自理能力的组合情况
        for i, j in od.groupby([count_tmp2[header[index[0]]], count_tmp2[header[index[1]]]]):
            if i[1] not in x:
                x.append(i[1])
            y2[i] = j.iloc[:, 0].size

            if i[0] not in z:
                z.append(i[0])
        # print(y2)
        # y2 = list(y2)

        for x1 in x:
            for z1 in z:
                w.append((z1, x1))
                if (z1, x1) not in list(y2):
                    # y2.insert(x.index(x1) * len(x) + z.index(z1), (z1, x1))
                    y2[(z1, x1)] = 0

        idx = 0
        yy = np.zeros(len(z) * len(x), dtype=int)  # 创建一个全0的数组，数组的长度是len(z)*len(x)
        for i in sorted(y2.keys()):  # sorted 排序
            yy[idx] = y2[i]
            idx += 1

        yy.resize((len(z), len(x)))  # 将yy转换成len(z)行 len(x)列的数组
        # print(sorted(x))
        # print(yy[0, :])
        # print(yy[1, :])
        return sorted(x),yy,yy[0,:],yy[1,:],z

# my_c = CSVPlotter('older.csv')
# index = (1,9)
# cc = my_c.get1dcolumn(index)
# index = (9,12)
# ff = my_c.get2dcolumn(index)
# print(cc)
# print(ff[3])



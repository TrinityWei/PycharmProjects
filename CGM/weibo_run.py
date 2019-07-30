# Author: Wei Meng-Xin
# E-mail: weimengxin2012@hotmail.com
# Time: 10/13/2018
# Tool: Pycharm 2018.2
# 该文件是运行文件

import multiprocessing as mp
import weibo
import time


def read_csv(name):
    '''该函数读取CSV文件数据'''
    import csv
    csv_file = csv.reader(open("/Users/mengxinwei/Downloads/" + name + ".csv", "r"))
    object_website = []
    for i in csv_file:
        object_website.append(i)
        # print(i)
    return object_website


if __name__ == "__main__":
    # 多进程并发
    object_location = []
    location = read_csv("weibo")
    for i in location[1:]:
        if i[1] not in object_location:
            if i[1] != "习水县":
                object_location.append(i[1])

    # obj = object_location[6::8]
    # obj_1 = obj[1::4][0::2]
    # object_location.remove("习水县")

    test = object_location[2::10]

    data_1 = []
    start = time.time()
    pool = mp.Pool()
    res_uid = pool.map(weibo.search_weibo, object_location[1::10])
    data_1.append(res_uid)
    end = time.time()
    print("总共耗时：%f" % (end - start))




    data_5 = []
    start = time.time()
    for l in object_location[1885::10]:
        res = weibo.search_weibo(l)
        data_5.append(res)
    end = time.time()
    print("总共耗时：%f" % (end - start))


object_location.index("宛城区")



data = []
data.extend(data_0[0])
data.extend(data_1[0])
data.extend(data_2[0])
data.extend(data_3[0])
data.extend(data_4[0])
data.extend(data_5[0])
data.extend(data_6[0])
data.extend(data_7[0])
data.extend(data_8[0])
data.extend(data_9[0])







def data_clear(location):
    '''该函数将爬取的发微博的时间改为具体年份'''
    years = []
    all_year = []
    for s in location:
        for item in location[s]:
            for sd in item:
                years.append(s)
                years.append(sd)
                for yr in item[sd]:
                    if len(yr) <= 9:
                        years.append("2019")
                    elif len(yr) == 10:
                        years.append(yr[0:4])
                    elif yr == '抱歉，未找到相关结果。':
                        years.append("NaN")
                all_year.append(years.copy())
                years.clear()
    return all_year


def count_fun(list_set):
    '''该函数统计各年的关键字数量'''
    from collections import Counter
    count_set = []
    for it in list_set:
        count = Counter(it)
        count_dict = dict(count)
        count_set.append(count_dict)
    return count_set


def output_table(list_set):
    '''该函数将数据整理为我们数据的v表格形式'''
    year_obj = []
    contains = []
    ye = ["2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009"]
    for ti in ye:
        contains.append(tuple(list_set[0].keys())[0])
        contains.append(ti)
        for wei in list_set:
            # title = wei[keyss]
            try:
                counts = wei[ti]
                contains.append(counts)
            except KeyError:
                counts = "NaN"
                contains.append(counts)
        year_obj.append(contains.copy())
        contains.clear()
    return year_obj


def get_data(list_set):
    '''该函数获取单个地区、单个年份的按 output_table 函数格式化后的数据'''
    all_year = data_clear(list_set)
    count_set = count_fun(all_year)
    year_obj = output_table(count_set)
    return year_obj


set_final = []
for items in data:
    year_obj = get_data(items)
    set_final.extend(year_obj)

for k in set_final:
    if k[1] == "2019":
        set_final.remove(k)


def output_data(all_data, output_file_name):
    '''该函数将最终数据输出为CSV文件'''
    import pandas as pd
    name = ["地区", "年份", "政绩工程", "形象工程", "面子工程", "贴金工程", "门面工程", "首长工程", "白象工程", "形式主义", "官僚主义", "劳民伤财"]
    table = pd.DataFrame(columns=name, data=all_data)
    # table = pd.DataFrame(data=all_data)
    table.to_csv("/Users/mengxinwei/Downloads/" + output_file_name + ".csv")
    return table

re = output_data(set_final, "weibo_all")




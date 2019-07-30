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
    location_1 = []
    location = read_csv("weibo")
    for i in location[1:]:
        location_1.append(i[1])

    object = []
    for k in location_1:
        if k not in object:
            object.append(k)

    # obj = object_location[6::8]
    # obj_1 = obj[1::4][0::2]
    # object_location.remove("习水县")

    start = time.time()
    pool = mp.Pool()
    res_uid_0 = pool.map(weibo.search_weibo, object[0:51])
    end = time.time()
    print("总共耗时：%f" % (end - start))


# method为多次调用的方法


if __name__ == '__main__':
    location_1 = []
    location = read_csv("weibo")
    for i in location[1:]:
        location_1.append(i[1])

    object = []
    for k in location_1:
        if k not in object:
            object.append(k)

    data_1 = []
    pool = mp.Pool(processes=6)
    for param in object[1001:2001]:
        data_1.append(pool.apply_async(weibo.search_weibo, args=(param,)))

    pool.close()
    pool.join()


def data_arrange(data):
    import json
    import requests
    data_set = []
    for ps in data:
        try:
            data_set.append(ps.get())
        except json.decoder.JSONDecodeError:
            pass
        except requests.exceptions.SSLError:
            pass
    return data_set


def data_tran(text):
    loca = tuple(text.keys())[0]
    data = text[loca]
    res = []
    contain = []
    for it in data:
        keys = tuple(it.keys())[0]
        te = it[keys]
        for t in te:
            res.append(loca)
            res.append(keys)
            res.extend(t)
            middle = res.copy()
            contain.append(middle)
            res.clear()
    print(contain)
    return contain


def data_output(data):
    res = []
    data_sets = data_arrange(data)
    for it in data_sets:
        out = data_tran(it)
        res.extend(out)
    for g in res:
        if len(g) > 4:
            g.remove("NaN")
    return res


def output_data(all_data, output_file_name):
    '''该函数将最终数据输出为CSV文件'''
    import pandas as pd
    name = ["location", "keyword", "date", "text"]
    table = pd.DataFrame(columns=name, data=all_data)
    table.to_csv("/Users/mengxinwei/Downloads/" + output_file_name + ".csv")
    return table


###############################

data_final = data_output(data_1)
for g in data_final:
    if len(g) > 4:
        g.remove("NaN")
s = output_data(final_2000, "Weibo_RawText_2000")


def read_csv(name):
    '''该函数读取CSV文件数据'''
    import csv
    csv_file = csv.reader(open("/Users/mengxinwei/Downloads/" + name + ".csv", "r"))
    object_website = []
    for i in csv_file:
        object_website.append(i)
        # print(i)
    return object_website


data_set_1000 = []
for j in final_1000[1:]:
    data_set_1000.append(j[1:])

data_set_2000 = final_2000.copy()

data_set_3000 = []
for j in final_3000[1:]:
    data_set_3000.append(j[1:])

all_data = []
all_data.extend(data_set_1000)
all_data.extend(data_set_2000)
all_data.extend(data_set_3000)
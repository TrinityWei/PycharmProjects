# Author: Wei Meng-Xin
# E-mail: weimengxin2012@hotmail.com
# Time: 10/12/2018
# Tool: Pycharm 2018.2
# 该文件是主程序文件

# 运行说明：
# 1. 运行本程序前需安装Python requests库，可以在命令提示符窗口中输入：pip3 install requests 来完成安装，前提是已经配置好python和pip环境；
# 2. 通过 weibo_search_run.py 文件运行全部程序；
# 3. 请务必将 weibo_search.py 和 weibo_search_run.py 文件放到python同一个目录下，或者你可以在IDE中新建两个空文件，再将两份code分别复制进去也可


def quote_func(location, keywords):
    '''该函数将汉字转化为http可用的utf编码'''
    from urllib.request import quote
    url = "https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D" + location + "+" + keywords + "%26t%3D0&page_type=searchall"
    http = quote(url, safe=";/?:@&=+$,", encoding='utf-8')
    return http


def login_weibo(location, keywords):
    '''这是个较复杂的主函数，负责爬取weibo的搜索数据'''
    import requests
    import time
    import random
    res = []
    contain = []
    res_dict = dict()
    addr = quote_func(location, keywords)
    # headers = [{'User-Agent': "Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko)"
    #                           " Chrome/69.0.3497.100 Safari/537.36",
    #             'Accept': 'text/html;q=0.9,*/*;q=0.8',
    #             'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    #             'Connection': 'close'}]
    headers = [{'User-Agent': "Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko)"
                              " Chrome/69.0.3497.100 Safari/537.36",
                'Accept': 'text/html;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Connection': 'close'},
               {'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1 (KHTML,"
                              " like Gecko) CriOS/69.0.3497.100 Mobile/13B143 Safari/601.1.4",
                'Accept': 'text/html;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Connection': 'close'},
               {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, "
                              "like Gecko) Version/7.0.3 Safari/7046A194A",
                'Accept': 'text/html;q=0.9,*/*;q=0,8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Connection': 'close'},
               {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
                'Accept': 'application/json, text/plain, */*',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Connection': 'close'},
               {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                'Accept': 'application/json, text/plain, */*',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Connection': 'close'}]
    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "H21HT1P7C30F1P5D"
    proxyPass = "8F451A3BD7C939D0"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host": proxyHost,
      "port": proxyPort,
      "user": proxyUser,
      "pass": proxyPass,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }

    k = 1
    try:
        while True:
            urls = addr + "&page=" + str(k)
            # print(urls)
            s = requests.Session()
            s.keep_alive = False
            ob = s.get(urls, headers=random.choice(headers), proxies=proxies, allow_redirects=False).json()
            time.sleep(0.5 + random.random())
            if ob["ok"] == 1:
                try:
                    if ob["data"]["cards"][0]["desc"] == "抱歉，未找到相关结果。":
                        res.append("NaN")
                except KeyError:
                    texts = ob["data"]["cards"]
                    for i in texts:
                        try:
                            for w in i["card_group"]:
                                if w["card_type"] == 9 and w["mblog"]["user"]["verified_type"] != 1:
                                    time_obj = w["mblog"]["created_at"]
                                    res.append(time_obj)
                                    text_obj = w["mblog"]["text"]
                                    res.append(text_obj)
                                    middle = res.copy()
                                    contain.append(middle)
                                    res.clear()

                        except KeyError:
                            if i["card_type"] == 9 and i["mblog"]["user"]["verified_type"] != 1:
                                time_obj = i["mblog"]["created_at"]
                                res.append(time_obj)
                                text_obj = i["mblog"]["text"]
                                res.append(text_obj)
                                middle = res.copy()
                                contain.append(middle)
                                res.clear()
                k += 1
                s.close()
            elif ob["msg"] == "这里还没有内容":
                # print("这里没有内容")
                s.close()
                break
        res_dict[keywords] = contain
        return res_dict
    except requests.exceptions.ProxyError:
        return login_weibo(location, keywords)


def search_weibo(local):
    '''该函数负责遍历所有关键字，这些关键字可以自定义'''
    res = []
    result = dict()
    # keys = ["电子政务", "政务公开", "政务服务", "行政职权", "腐败", "反腐", "监督", "政务平台", "行政体制", "服务型政府",
    #         "依法行政", "阳光施政", "政务服务试点", "行政权力", "公开", "透明", "电子政务平台", "信息共享", "政府信息",
    #         "便民服务", "职权法定", "权责一致", "监察", "政务网络", "政府网站", "廉政"]
    # keys = ["教育", "基础教育", "在校学生", "中学", "小学", "医院", "医疗", "床位", "社会福利", "福利院", "基础设施投资",
    #         "固定资产投资", "工业用地", "土地拍卖", "协议转让", "土地价格", "政企合谋", "管理费用", "官商勾结"]
    keys = ["基本建设", "基础设施", "固定资产投资", "交通", "电信", "电网", "电力", "公共服务", "政务公开", "政务服务", "公开透明",
            "腐败", "反腐", "廉政", "政企合谋", "官商勾结"]
    for word in keys:
        keyword = login_weibo(local, word)
        res.append(keyword)
        print("-{ %s }-关键字-{ %s }-检索完毕：共%d个" % (local, word, len(keyword[word])))
    result[local] = res
    return result


def output_data(all_data, output_file_name):
    '''该函数将最终数据输出为CSV文件'''
    import pandas as pd
    name = ["location", "keyword", "date", "text"]
    table = pd.DataFrame(columns=name, data=all_data)
    table.to_csv("/Users/mengxinwei/Downloads/" + output_file_name + ".csv")
    return table


def read_csv(name):
    '''该函数读取CSV文件数据'''
    import csv
    csv_file = csv.reader(open("/Users/mengxinwei/Downloads/" + name + ".csv", "r"))
    object_website = []
    for i in csv_file:
        object_website.append(i)
        # print(i)
    return object_website





import urllib
import urllib3
import ssl
import json
import re
import weibo
import time
import multiprocessing as mp
import random


def get_sentiment(text):
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib3.disable_warnings()
    ###第一步：获取access_token
    host_1 = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=pd152AVsnYc6Nbfk5Yuh9XTh&client_secret=ZTn7ASCKAGgPFEFmMxszEoQmAlVb2LRM'
    host_2 = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=ey1TmLzsqex8xLj9GqUm4duk&client_secret=IWYngrCEAloVNN4as3hvYZoiZsjn9tjU'
    host_3 = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=2k9jRqGNe6HIpXTPWxg7OHNx&client_secret=MbyPEaG9FzXBzq7x9f74ADSZeaEmu74c'
    host_4 = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=NxBlWntWC2QgjCDCYt4S9QVQ&client_secret=7F2Wq5RYDGh3Ec1vARj8gyAtUMHRuvEy'
    host_5 = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=X6ZQp3YE9IzNrzzVUiEyozMK&client_secret=yEPwwgf2DpZsM0hRjnVgaC8OOpw3tf6I'
    host = random.choice([host_1, host_2, host_3, host_4, host_5])
    time.sleep(0.05)
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    # if (content):
    #     print(type(content))  # <class 'bytes'>
    content_str = str(content, encoding="utf-8")
    content_dir = eval(content_str)
    access_token = content_dir['access_token']
    ### 第二步：获取
    # print(sys.getdefaultencoding())
    http = urllib3.PoolManager()
    url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?access_token="+access_token
    # print(url)
    data = {"text": text}
    encode_data = json.dumps(data).encode('GBK')
    #JSON:在发起请求时,可以通过定义body 参数并定义headers的Content-Type参数来发送一个已经过编译的JSON数据：
    request = http.request('POST',
                           url,
                           body=encode_data,
                           headers={'Content-Type': 'application/json'}
                           )
    res_0 = request.data.decode("GBK")[-4]
    return res_0


def regulation(input):
    from bs4 import BeautifulSoup
    words = BeautifulSoup(input, "lxml").get_text()
    print(words)
    return words


def get_pure_data(data):
    contain = []
    for i in data[1:]:
        res = i[1:-1]
        text = regulation(i[-1])
        res.append(text)
        middle = res.copy()
        contain.append(middle)
        res.clear()
    return contain


data = weibo.read_csv("Weibo_RawText_Data")
new_weibaoRawText = get_pure_data(data)



def get_sent(it):
    try:
        final_data = []
        final = it.copy()
        sent = get_sentiment(final[-1])
        final.append(sent)
        middle = final.copy()
        print(middle)
        final_data.append(middle)
        return final_data[0]
    except IndexError:
        time.sleep(3)
        return get_sent(it)
    except urllib.error.HTTPError:
        time.sleep(3)
        return get_sent(it)
    except:
        time.sleep(20)
        return get_sent(it)



# data_3 = []
# pool = mp.Pool(processes=3)
# for param in new_weibaoRawText[20001:40001]:
#     data_3.append(pool.apply_async(get_sent, args=(param,)))
#
# pool.close()
# pool.join()

start = time.time()
pool = mp.Pool(5)
res_4 = pool.map(get_sent, new_weibaoRawText[300001:])
end = time.time()
print("总共耗时：%f" % (end - start))


data_set = []
data_set.extend(res_1)
data_set.extend(res_2)
data_set.extend(res_3)
data_set.extend(res_4)







data_1 = []

start = time.time()
for param in new_weibaoRawText[90001:100001]:
    data_1.append(get_sent(param))
end = time.time()
print("耗时： %f" % (end - start))


def output_data(all_data, output_file_name):
    '''该函数将最终数据输出为CSV文件'''
    import pandas as pd
    name = ["location", "keyword", "date", "text", "sentiment"]
    table = pd.DataFrame(columns=name, data=all_data)
    table.to_csv("/Users/mengxinwei/Downloads/" + output_file_name + ".csv")
    return table


r = output_data(new_data, "Weibo_BaiduAPI_Sentiment_DataSet")



data_1 = read_csv("Weibo_BaiduAPI_Sentiment_25000")
data_2 = read_csv("Weibo_BaiduAPI_Sentiment_35058")
data_3 = read_csv("Weibo_BaiduAPI_Sentiment_90000")
data_4 = read_csv("Weibo_BaiduAPI_Sentiment_130001")
data_5 = read_csv("Weibo_BaiduAPI_Sentiment_200001")
data_6 = read_csv("Weibo_BaiduAPI_Sentiment_300001")
data_7 = read_csv("Weibo_BaiduAPI_Sentiment_end")


all_data = []
for i in data_7[1:]:
    all_data.append(i[1:])


except_data = []
for k in all_data:
    if k[-1] == 'e':
        except_data.append(k[:-1])

start = time.time()
pool = mp.Pool(3)
res_4 = pool.map(get_sent, except_data)
end = time.time()
print("总共耗时：%f" % (end - start))


new_data = []
for n in all_data:
    if n[-1] != 'e':
        new_data.append(n)

for n in res_4:
    if n[-1] != 'e':
        new_data.append(n)

new_data.extend(last)

special = []
for n in res_4:
    if n[-1] == 'e':
        special.append(n[:-1])


last = []
start = time.time()
for param in special:
    last.append(get_sent(param))
end = time.time()
print("耗时： %f" % (end - start))






for m in new_data:








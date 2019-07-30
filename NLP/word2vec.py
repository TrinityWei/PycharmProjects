

import time  # 插入time库，记录程序运行时间
from gensim.corpora import WikiCorpus  #


def xml_to_txt(input_path, output_file):
    '''该函数负责将下载的XML文件转换成txt文件'''
    start = time.time()
    i = 0
    space = " "
    output = open(output_file, 'w')
    wiki = WikiCorpus(input_path, lemmatize=False, dictionary=[])  # gensim里的维基百科处理类WikiCorpus
    for text in wiki.get_texts():  # 通过get_texts将维基里的每篇文章转换位1行txt文本，并且去掉了标点符号等内容
        output.write(space.join(text) + "\n")
        i = i+1
        if i % 2000 == 0:  # 每转换好2000个文章，提示我们并记录运行时间
            now = time.time()
            print("Finished Saved %s articles and Time consuming: %f 秒" % (i, (now - start)))
    output.close()
    end = time.time()
    print("Finished Saved %s articles and Time consuming: %f 秒" % (i, (now - start)))
    return output_file


inputs = "/Users/mengxinwei/Downloads/zhwiki-latest-pages-articles.xml.bz2" # 这是下载好的wiki语料库的路径，请改成你自己电脑的存放路径
outputs = "/Users/mengxinwei/Downloads/zhwiki.txt" # 这是保存转成txt文件的路径

get_text = xml_to_txt(inputs, outputs)  # 最后，我们调用该函数






import zhconv
import time

def convert_to_simpChinese(input_tradChinese_path, out_simpChinese_path):
    start = time.time()
    with open(input_tradChinese_path, 'r', encoding='UTF-8') as f:
        content = f.read()
        print("读取完毕！")
        with open(out_simpChinese_path, 'w', encoding='UTF-8') as f1:
            print("正在转换....")
            f1.write(zhconv.convert(content, 'zh-cn'))
    end = time.time()
    print("Finished converted and Time consuming: %f 秒" % (end - start))


inputs = "/Users/mengxinwei/Downloads/zhwiki.txt"  # 这是包含繁体中文的txt格式的语料库
outputs = "/Users/mengxinwei/Downloads/zhwiki_simp.txt"  # 这是转成简体txt文件的保存路径

convert_to_simpChinese(inputs, outputs)






import codecs
f = codecs.open("/Users/mengxinwei/Downloads/zhwiki_simp.txt", "r", encoding = "utf8")
line = f.readline()
print(line)





import jieba
import codecs
import time






#!/usr/bin/env python
# -*- coding: utf-8  -*-
#测试训练好的模型

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')  # 忽略警告
import gensim


if __name__ == '__main__':
    model = gensim.models.Word2Vec.load("/Users/mengxinwei/Downloads/wiki.zh.text.model")

    word = model.most_similar("股票")
    for t in word:
        print(t[0], t[1])


    word = model.most_similar(positive=[u'皇上',u'国王'],negative=[u'皇后'])
    for t in word:
        print(t[0], t[1])

    word = model.most_similar(positive=[u'皇帝',u'国王'],negative=[u'皇后'])
    for t in word:
        print(t[0], t[1])


    print(model.doesnt_match(u'飞机 苹果 香蕉 火龙果 橘子 榴莲'.split()))
    print(model.doesnt_match(u'太后 皇贵妃 贵妃 妃子 贵人'.split()))


    print(model.similarity(u'经济', u'金融'))
    print(model.similarity(u'经济', u'央行'))
    print(model.similarity(u'经济', u'银行'))
    print(model.similarity(u'经济', u'计算机'))
    print(model.similarity(u'经济', u'睡觉'))
    print(model.similarity(u'经济', u'逛街'))





# !/usr/bin/env python
# -*- coding: utf-8  -*-
# 使用gensim word2vec训练脚本获取词向量

import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')  # 忽略警告

import logging
import os.path
import sys
import multiprocessing
import time

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    start = time.time()
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # inputs为输入语料, output_model为输出模型, output_vector为word2vec的vector格式的模型
    inputs = "/Users/mengxinwei/Downloads/zhwiki_simp_seg.txt"
    output_model = "/Users/mengxinwei/Downloads/wiki.zh.text.model"
    output_vector = "/Users/mengxinwei/Downloads/wiki.zh.text.vector"

    # 训练skip-gram模型
    model = Word2Vec(LineSentence(inputs), sg=1, size=300, window=4, min_count=5,
                     workers=multiprocessing.cpu_count())
    # 保存模型
    model.save(output_model)
    model.wv.save_word2vec_format(output_vector, binary=False)
    end = time.time()
    print("Data set training completed and Time consuming %s 秒" % (end - start))


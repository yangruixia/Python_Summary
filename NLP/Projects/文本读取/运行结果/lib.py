import os
import re
import json
import jieba
import pandas as pd

def name_lst(file_name):
    '''
    制作文件名列表      读入文件夹名字 返回其中文件名列表
    '''
    path = file_name
    existed_name_lst = []
    for i in os.listdir(path):
        dealed_name = i
        existed_name_lst.append(dealed_name)
    return existed_name_lst

def extract_content(name,file_name):
    '''
    抽取特定文件夹file_name中的特定文件name     返回文件内容    针对ANSI格式的文档
    '''
    fpath = '../' + file_name + '/' + name
    f = open(fpath)
    text = f.read() 
    return text

def extract_utf8_content(name,file_name):
    '''
    抽取特定文件夹file_name中的特定文件name     返回文件内容    针对utf-8格式的文档
    '''
    fpath = '../' + file_name + '/' + name
    f = open(fpath,encoding='utf-8')
    text = f.read() 
    return text

def write_into(file_name, content):
    '''
    将内容content写入名为file_name的文件
    '''
    with open(file_name, "w",encoding='utf-8') as f:
        json.dump(content, f,ensure_ascii=False,indent = 4)
    return ''

def extract_en(name,file_name):
    '''
    抽取特定文件夹file_name中的特定文件name中的所有英文     并将内容写入txt文件，后缀名为_EN.txt
    '''
    text = extract_content(name,file_name)
    uncn = re.compile(r'[\u0061-\u007a,\u0020]')
    text_en = ''.join(uncn.findall(text.lower()))
    file_en_name = name[:-4]+'_EN.txt'
    write_into(file_en_name, text_en)
    return ''

def extract_zh(name,file_name):
    '''
    抽取特定文件夹file_name中的特定文件name中的所有中文     并将内容写入txt文件，后缀名为_CN.txt
    '''
    text = extract_content(name,file_name)
    uncn = re.compile(r'[\u4e00-\u9fa5]')
    text_zh = ''.join(uncn.findall(text))
    file_zh_name = name[:-4]+'_CN.txt'
    write_into(file_zh_name, text_zh)
    return ''

def count_zh(name,file_name):
    '''
    使用jieba进行中文分词并进行词频统计
    '''
    text = extract_utf8_content(name,file_name)
    text=jieba.cut(text)
    counts = {}
    for word in text:
        rword = word
        counts[rword] = counts.get(rword,0) + 1
    li = list(counts.items())
    li.sort(key=lambda x:x[1], reverse=True)
    # 记录count结果到txt
    file_zh_name = name[:-4]+'_count.txt'
    write_into(file_zh_name, li)
    return li                       # 返回每个文件的（词，词频）列表

def count_en(name,file_name):
    '''
    进行英文分词并进行词频统计
    '''
    text = extract_utf8_content(name,file_name)
    words=text.split()  # 英文分词
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    li = list(counts.items()) # tuple("词":"词频")
    li.sort(key=lambda x:x[1], reverse=True)
    file_en_name = name[:-4]+'_count.txt'
    write_into(file_en_name, li)
    return li                       # 返回每个文件的词，词频

def to_csv(my_list,name, pathcsv):
    '''
    保存成为csv文件
    '''
    head = ['words','number']
    fpath = pathcsv + '/' + name[:-4] +'.csv'
    test = pd.DataFrame(columns = head,data = my_list)
    test.to_csv(fpath,encoding = 'gbk')

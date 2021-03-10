#-*- coding:utf-8 -*-
import os
import re
import json
import sys

def name_lst():#制作文件名列表
    existed_name_lst = []
    for i in os.listdir():
        dealed_name = i
        existed_name_lst.append(dealed_name)
    return existed_name_lst

def exam_name(name):#检验文件是否存在
    value = True
    existed_name_lst = name_lst()
    try:
        for i in existed_name_lst:
            if name == i:
                value = False
                break
        if(value):
            raise ValueError
    except ValueError as e:
        print('文件名'+ name +'无效！',e)


def extract_content(name):
    fpath = name
    f = open(fpath,)
    text = f.read()
    return text

def extract_en(name):
    text = extract_content(name)
    uncn = re.compile(r'[\u0061-\u007a,\u0020]')
    text_en = ''.join(uncn.findall(text.lower()))
    file_en_name = name[:-4]+'_EN.txt'
    with open(file_en_name, "w",encoding='utf-8') as f:
        json.dump(text_en, f,ensure_ascii=False,indent = 4)
    return ''

def extract_zh(name):
    text = extract_content(name)
    uncn = re.compile(r'[\u4e00-\u9fa5]')
    text_zh = ''.join(uncn.findall(text))
    file_zh_name = name[:-4]+'_CN.txt'
    with open(file_zh_name, "w",encoding='utf-8') as f:
        json.dump(text_zh, f,ensure_ascii=False,indent = 4)
    return ''

def main(argv):
    for name in argv[1:]:#除去运行文件
        try:
            exam_name(name)
            extract_en(name)
            extract_zh(name)
        except:
            continue
    return ''

if __name__ == '__main__':
    main(sys.argv)
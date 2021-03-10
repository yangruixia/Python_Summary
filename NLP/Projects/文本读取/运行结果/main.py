import os
import sys
import lib

def Read(file_name):
    '''
    分离英文文本和中文文本
    '''
    lst = lib.name_lst(file_name)
    rawpath = os.getcwd() 
    pathzh = rawpath + '/output_zh'
    pathen = rawpath + '/output_en'
    try:                            # 异常处理
        os.mkdir(pathzh)
        os.mkdir(pathen)
    except:
        pass
    for name in lst:
        try:
            os.chdir(pathen)
            lib.extract_en(name,file_name)
            os.chdir(pathzh)
            lib.extract_zh(name,file_name)
        except:
            continue
    os.chdir(rawpath)
    return ''

def CountZh():
    '''
    中文词频统计
    '''
    rawpath = os.getcwd()
    pathzh = rawpath + '/output_zhcount'
    pathzhcsv = rawpath + '/output_zhcount_csv'
    target_file_name = '/output_zh'
    lst = lib.name_lst(rawpath + target_file_name)
    try:
        os.mkdir(pathzh)
        os.mkdir(pathzhcsv)
    except:
        pass
    for name in lst: 
        try:
            os.chdir(pathzh)
            li = lib.count_zh(name,target_file_name)   # 所有列表的总和，包含所有文件的（词，词频）列表
            lib.to_csv(li,name,pathzhcsv)
            os.chdir(rawpath)        
        except:
            continue
    return ''

def CountEn():
    '''
    英文词频统计
    '''
    rawpath = os.getcwd() 
    pathen = rawpath + '/output_encount'
    pathencsv = rawpath + '/output_encount_csv'
    target_file_name = '/output_en'
    lst = lib.name_lst( rawpath + target_file_name)
    try:
        os.mkdir(pathen)
        os.mkdir(pathencsv)
    except:
        pass
    for name in lst:
        try:
            os.chdir(pathen)
            li=lib.count_en(name,target_file_name) # 文件的词，词频总和
            lib.to_csv(li,name,pathencsv)   # csv函数加在这里（参数使用li）
            os.chdir(rawpath)
        except:
            continue
    return ''

def main(file_name):
    Read(file_name)
    CountZh()
    CountEn()

if __name__ == '__main__':
    file_name = sys.argv[1]
    main(file_name)
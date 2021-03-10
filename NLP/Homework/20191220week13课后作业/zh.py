# 英文文本分析

# 源文本格式：rtf
# 分析内容：统计英文单词中名词、形容词、副词等占所有词汇的百分比。

# 技术路线：使用

def open_file(fname):
    '''
    打开文件
    '''
    with open(fname, 'r', encoding = 'utf-8')as file_object:
        contents = file_object.read()
    return contents

def count_freq(content):
    import jieba.posseg as pseg
    # from jieba import analyse
    from collections import Counter
    
    content = pseg.cut(content)
    # print(content)
    # print(dict(Counter(text)))
    # wordsCount = len(list(content))
    # text = dict(content)
    realtext = []
    for k,v in content:
        realtext.append(v)
    wordsCount = len(realtext)
    d = dict(Counter(realtext))
    my_list = []
    for key in d.keys():
        my_list.append([key,d[key]/wordsCount])
    # print(my_list)
    return my_list

    # print(text)
    # list = []
    # for k,v in text:
    #     list.append([k,v])
    # print(list)    

def write_to_file(list, file='《地球往事三部曲》result.txt'):
    f = open(file, 'w', encoding = 'utf-8')
    for item in list:
        f.write(str(item[0])+'：'+str(item[1])+'\n')


text = open_file('《地球往事三部曲》.txt')
# print(text)
freq_list = count_freq(text)
# print(freq_list)
# content = clear(text)
# freq_list = count_freq(content)
write_to_file(freq_list)
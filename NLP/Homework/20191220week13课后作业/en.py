# 英文文本分析

# 源文本格式：rtf
# 分析内容：统计英文单词中名词、形容词、副词等占所有词汇的百分比。

# 技术路线：使用

def open_file(fname):
    with open(fname, 'r')as file_object:
        contents = file_object.read()
    return contents

def clear(content):
    text1 = content.replace('\n', '')
    text2 = text1.replace("\'", "\'")
    text3 = text2.replace("\\", '')
    content = text3.replace('\\par', '')
    return content

def count_freq(content):
    import nltk
    from nltk.tokenize import word_tokenize
    token = word_tokenize(content)
    tagged = nltk.pos_tag(token)
    # print(tagged)

    wordsCount = len(tagged)
    # print(wordsCount)

    plt = nltk.FreqDist(text)
    # print('各个词性标注统计结果')
    # print(plt)
    d = dict(plt)
    list = []
    for key in d.keys():
        list.append([key,d[key]/wordsCount])
    return list

def write_to_file(list, file='results_en.txt'):
    f = open(file, 'w', encoding = 'utf-8')
    for item in list:
        f.write(str(item[0])+'：'+str(item[1])+'\n')


text = open_file('Pullman, Philip - His Dark Materials, Book 1.rtf')
content = clear(text)
freq_list = count_freq(content)
write_to_file(freq_list)
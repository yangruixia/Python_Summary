import requests
import random
import time
import pandas as pd
from pyquery import PyQuery as pq
import os


def FangHTMLDl(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()#如果状态码不是200，将会产生异常
        # r.encoding = r.apparent_encoding
        r.encoding='gbk'             # 使用gbk编码
        doc = pq(r.text)
        return doc          # 返回pyquery之后的值
    except:
        return '产生异常'

class BaseExtrator():   # 网页内容抓取的初步处理
    def __init__(self,html='<html></html>'):
        self.doc = pq(html)

class FangNavExt(BaseExtrator):     # 返回nav的所有链接
    def __init__(self,html):
        super(FangNavExt,self).__init__(html)

    def parse(self):
        lis = self.doc('#quyu_name>a')
        # 自定义需要爬取的地区
        location=['朝阳','海淀','丰台','西城','东城','昌平','大兴','通州','房山','顺义','石景山','密云','门头沟','怀柔','延庆','平谷','燕郊','北京周边']
        Nav_links = []
        furl='https://newhouse.fang.com'
        for i in range(0,len(lis)):
            pq_li = pq(lis[i])
            area = pq_li.text()
            link = furl + pq_li.attr('href')
            if area in location:
                Nav_links.append([area,link])
            else:
                pass
        return Nav_links

class FangPageExt(BaseExtrator):    # 返回page的所有链接（需要判断是否为有效链接，根据是否含有名字进行判断）
    def __init__(self,html):
        super(FangPageExt,self).__init__(html)
    def parse(self):
        lis = self.doc('.page>ul>li>a')
        # print(lis)
        furl='https://newhouse.fang.com'
        Nav_links = []
        for i in range(1,len(lis)-2):
            pq_li = pq(lis[i])
            link = furl + pq_li.attr('href')
            Nav_links.append(link)
        return Nav_links

class FangMsgExt(BaseExtrator):     # 返回信息lists  
    def __init__(self,html):
        super(FangMsgExt,self).__init__(html)
    def parse(self):
        lis = self.doc('#newhouse_loupai_list>ul>li>.clearfix')

        Message_lists = []
        for i in range(0,len(lis)):
            pq_li = pq(lis[i])
            house_name = pq_li.find('.nlcd_name').text()
            house_type = pq_li.find('.house_type.clearfix').text()
            house_address = pq_li.find('.address').text()
            house_tel = pq_li.find('.tel').text()
            house_price = pq_li.find('.nhouse_price').text()
            # house_price = house_price.replace('�O','m^2')       # 修改乱码       # 后来发现在前面使用gbk编码即可
            # print(house_name,house_type,house_address,house_tel,house_price)
            Message_lists.append([house_name,house_type,house_address,house_tel,house_price])
        return Message_lists

def GetNav(url):
    html_text = FangHTMLDl(url)
    NavExt = FangNavExt(html_text)
    nav = NavExt.parse()
    return nav

def GetPage(url):
    html_text = FangHTMLDl(url)
    PageExt = FangPageExt(html_text)
    page_list = PageExt.parse()
    return page_list

def GetInfo(url):
    html_text = FangHTMLDl(url)
    MessageExt = FangMsgExt(html_text)
    info = MessageExt.parse()
    return info

#以csv文件保存数据
def to_csv(area,infos):
    area =area
    lst = infos
    head = ['residentian_area','rooms_area','address','telephone','price']
    rawpath = os.getcwd()
    fpath = rawpath + '/results/' + area +'.csv'#fpath可自行指定
    test = pd.DataFrame(columns=head,data=lst)
    test.to_csv(fpath,encoding='gbk')
    return ''

init_url = 'https://newhouse.fang.com/house/s'

nav_links = GetNav(init_url)
rawpath = os.getcwd()
fpath = rawpath + '/results'
try:
    os.mkdir(fpath)
except:
    pass
for nav_link in nav_links:
    area = nav_link[0]                      # 地区变量，以便给未来的csv文件进行命名
    page_links = [nav_link[1]]
    other_pages_link = GetPage(nav_link[1])
    total_infos = []                        # 存放每一个区域总共的信息
    for i in other_pages_link:
        page_links.append(i)
    for each in page_links:
        detail_info = GetInfo(each)         # 每一页的信息
        for info in detail_info:
            if (info[0] == ''):
                continue
            else:
                total_infos.append(info)
    try:
        to_csv(area,total_infos)
    except:
        pass
    '''
        此处加入插入csv文件的函数，参数为area和total_infos
        注意csv文件编码使用gbk，否则会出现乱码
    '''

    # 以下为打印测试使用
    #for i in range(0,len(total_infos)):
    #    print(i,total_infos[i])
    #print('======================================')

'''
总结：
1.获取网页的函数采用相同的函数
2.获取网页时需注意编码问题，因为小区名称经常有生僻字，而且平方米的表达也需要复杂编码的支撑
3.采用类的方法，在基类的基础上分别写获取导航栏链接，分页的链接，以及具体的信息的子类
4.获取信息时出现空字符串情况，所以在主函数中进行判断
'''
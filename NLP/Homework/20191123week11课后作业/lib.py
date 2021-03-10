import requests
from pyquery import PyQuery as pq
import re
import time # 用于调节时间的模块导入
import random

class ProxyPool():
    def __init__(self):
        # 初始化读取proxy站点配置文件

        # 初始化读取proxy池存储位置（文件、数据库、NoSQL...)

        # 定时扫描proxy可用性、删除失效代理
        pass

    def check_a_proxy(self):
        pass

class KKBaseDownloader():
    def __init__(self):
        # 初始化代理池对象
        self.proxyp = ProxyPool()
        # 初始化headers配置列表文件路径
        self.headers_cfg_pth=''
        # 初始化最小、最大暂停间隔
        self.interval_min_max = (5,30)
        pass
    
    def gen_an_ua(self):
        self.ua_list = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0"]

        return random.choice(self.ua_list)

    def get_a_proxy(self):
        proxys = [

        ]
        idx = random.randint(1,len(proxys))
        return proxys[idx]

class KKNavDl(KKBaseDownloader):
    def __init__(self,init_url):
        super(KKNavDl,self).__init__()
        self.url_tgt = init_url

    def fetch_html(self):
        ua = self.gen_an_ua()
        headers = {'User-Agent':ua}
        # _proxy = self.get_a_proxy()
        # r = requests.get(self.url_tgt,proxies=_proxy)
        r = requests.get(self.url_tgt,headers=headers)
        if r.status_code==200:
            if r.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(r.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r.apparent_encoding
            encode_content = r.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            return encode_content
        else:
            return ''

class KKPageDl(KKBaseDownloader):
    def __init__(self,init_url):
        super(KKPageDl,self).__init__()
        self.url_tgt = init_url

    def fetch_html(self):
        ua = self.gen_an_ua()
        headers = {'User-Agent':ua}
        # _proxy = self.get_a_proxy()
        # r = requests.get(self.url_tgt,proxies=_proxy)
        r = requests.get(self.url_tgt,headers=headers)
        if r.status_code==200:
            if r.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(r.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r.apparent_encoding
            encode_content = r.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            return encode_content
        else:
            return ''

class KKPsgDl(KKBaseDownloader):
    def __init__(self,init_url):
        super(KKPsgDl,self).__init__()
        self.url_tgt = init_url  


    def fetch_html(self):
        ua = self.gen_an_ua()
        headers = {'User-Agent':ua}
        # _proxy = self.get_a_proxy()
        # r = requests.get(self.url_tgt,proxies=_proxy)
        r = requests.get(self.url_tgt,headers=headers)
        if r.status_code==200:
            if r.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(r.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r.apparent_encoding
            encode_content = r.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            return encode_content
        else:
            return ''

class ContentDl(KKBaseDownloader):
    def __init__(self,init_url):
        super(ContentDl,self).__init__()
        self.url_tgt = init_url  

    def fetch_html(self):
        ua = self.gen_an_ua()
        headers = {'User-Agent':ua}
        # _proxy = self.get_a_proxy()
        # r = requests.get(self.url_tgt,proxies=_proxy)
        r = requests.get(self.url_tgt,headers=headers)
        if r.status_code==200:
            if r.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(r.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r.apparent_encoding
            encode_content = r.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            return encode_content
        else:
            return ''

class KKBaseExtractor():
    def __init__(self,html='<html></html>'):
        self.doc = pq(html)

class KKNavExt(KKBaseExtractor):
    def __init__(self,html):
        super(KKNavExt,self).__init__(html)

    def parse(self):
        lis = self.doc('.navtab>ul>li')
        nav_links = []
        for i in range(4,len(lis)-1):        # 指定栏目开始进行保存
            pq_li = pq(lis[i])
            url = 'http://www.kekenet.com' + pq_li.find('a').attr('href')
            nav_links.append((pq_li.text(), url))
        return nav_links

class KKPageExt(KKBaseExtractor):
    def __init__(self,html):
        super(KKPageExt,self).__init__(html)

    def parse(self):
        lis = self.doc('.page.th')
        page_links = []
        for i in range(0,len(lis)):
            pq_li = pq(lis[i])
            url = pq_li('a').eq(1).attr('href')
            num = re.findall(r'\d+', url)
            intnum = int(num[0]) # 使用正则表达式提取数字并转换为int格式，提取出总共有多少页
            for i in range(1,intnum+2):  # +2是为了进行边界调节
                url = pq_li('a').eq(1).attr('href')
                true_url = 'http://www.kekenet.com' + url.replace(num[0],str(i))   # 注意str和int的转换
                page_links.append(true_url)
        return page_links
    
class KKPsgExt1(KKBaseExtractor): # h2中存在多个a标签，采用该方法
    def __init__(self,html):
        super(KKPsgExt1,self).__init__(html)
    
    def parse(self):
        lis1 = self.doc('.list_box_2>ul>li>h2')    # 抓取链接和title
        lis2 = self.doc('.list_box_2>ul>li>p') # 抓取其他信息
        nav_links = []
        for i in range(0,len(lis1)):
            pq_li1 = pq(lis1[i])
            pq_li2 = pq(lis2[i])
            # url.replace(' ','')
            other_info = pq_li2.text()
            # 获取时间
            time1 = ''
            time1 = other_info[0:other_info.rfind('编辑：')-1]   # 原始暴力方法消除空格
            # 获取编辑者
            author = ''
            author = other_info[other_info.rfind('编辑：')+3:other_info.rfind('标签：')-1]
            # 获取标签
            tag = ''
            tag = other_info[other_info.rfind('标签：')+4:]
            nav_links.append((pq_li1('a').eq(1).text(),pq_li1('a').eq(1).attr('href'),time1,author,tag))
        return nav_links

class KKPsgExt2(KKBaseExtractor):   # h2中仅仅存在一个a标签，采用该方法
    def __init__(self,html):
        super(KKPsgExt2,self).__init__(html)
    
    def parse(self):
        lis1 = self.doc('.list_box_2>ul>li>h2')      # 抓取链接和title
        lis2 = self.doc('.list_box_2>ul>li>p') # 抓取其他信息
        nav_links = []
        for i in range(0,len(lis1)):
            pq_li1 = pq(lis1[i])
            pq_li2 = pq(lis2[i])
            other_info = pq_li2.text()
            # 获取时间
            time1 = ''
            time1 = other_info[0:other_info.rfind('编辑：')-1]   # 原始暴力方法消除空格
            # 获取编辑者
            author = ''
            author = other_info[other_info.rfind('编辑：')+3:other_info.rfind('标签：')-1]
            # 获取标签
            tag = ''
            tag = other_info[other_info.rfind('标签：')+4:]
            nav_links.append((pq_li1.text(), pq_li1.find('a').attr('href'), time1, author,tag))
        return nav_links

class KKContentEnExt(KKBaseExtractor): # 英文获取   根据class
    def __init__(self,html):
        super(KKContentEnExt,self).__init__(html)
    
    def parse(self):
        lis = self.doc('#article_eng>div')
        contenten = ''
        contentzh = ''
        for i in range(0,len(lis)):
            pq_li = pq(lis[i])
            contenten += str(pq_li.find('.qh_en').text())
            contentzh += str(pq_li.find('.qh_zg').text())
            # time.sleep(random.random()*3) 
        return [contenten,contentzh]

# class KKContentZgExt(KKBaseExtractor): # 中文获取   根据class
#     def __init__(self,html):
#         super(KKContentZgExt,self).__init__(html)
    
#     def parse(self):
#         lis_zh = self.doc('#article_eng>div')
#         for i in range(0,len(lis_zh)):
#             contentzh = ''
#             pq_li_zh = pq(lis_zh[i])
#             contentzh += str(pq_li_zh.find('.qh_zg').text())
#         return contentzh

def GetNavLinks():  # 获取nav导航栏  
    navDl = KKNavDl(init_url='http://www.kekenet.com/read/news')
    html = navDl.fetch_html()
    navExt = KKNavExt(html)
    nav_links = navExt.parse()
    return nav_links

def GetPageLinks(nav):  # 获取某标题栏所有页面链接
    page = KKPageDl(init_url= nav[1])
    html = page.fetch_html()
    pageExt = KKPageExt(html)
    page_links = pageExt.parse()
    page_links.append(nav)
    return page_links

def GetPsgLink1(page_link): # 输入单独链接【采用方法1】传入文章列表
    psgDl = KKPsgDl(init_url= page_link)
    html = psgDl.fetch_html()
    psgExt = KKPsgExt1(html)
    psg_link = psgExt.parse()
    # psg_links.append(psg_link)
    time.sleep(random.random()*3)      # 控制时间
    return psg_link

def GetPsgLink2(page_link):  # 输入单独链接【采用方法2】传入文章列表
    psgDl = KKPsgDl(init_url=  page_link)
    html = psgDl.fetch_html()
    psgExt = KKPsgExt2(html)
    psg_link = psgExt.parse()
    # psg_links.append(psg_link)
    time.sleep(random.random()*3)       # 控制时间
    return psg_link

def GetContent(psg_link):
    contentDl = ContentDl (init_url = psg_link[1])
    html = contentDl.fetch_html()
    conExt = KKContentEnExt(html) # 获取英文
    contentall = conExt.parse()
    # conExtZh = KKContentZgExt(html) # 获取中文
    # contentzh_get = conExtZh.parse()
    # print(psg_link)
    if ((str(contentall[0]) == '') or(str(contentall[1]) == '')): # 判断是否有内容，没有内容进行跳过
        return ''
    else:
        # time.sleep(random.random()*3) 
        psg_title = psg_link[0]
        link = psg_link[1]
        psg_time = psg_link[2]
        psg_author = psg_link[3]
        psg_tag = psg_link[4]
        temp_dict = { 'title': psg_title, 'link': link, 'time': psg_time , 'author': psg_author, 'tag': psg_tag ,'en': str(contentall[0]), 'zh': str(contentall[1])}   # 'zh': str(contentzh_get
        return temp_dict

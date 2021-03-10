import requests
import random
import time
from pyquery import PyQuery as pq
import json

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

class KKPsgExt(KKBaseExtractor):
    def __init__(self,html):
        super(KKPsgExt,self).__init__(html)
    
    def parse(self):
        lis = self.doc('.list_box_2>ul>li>h2')
        nav_links = []
        for i in range(0,len(lis)):
            pq_li = pq(lis[i])
            nav_links.append((pq_li.text(), pq_li.find('a').attr('href')))
        return nav_links

class KKContentEnExt(KKBaseExtractor): # 英文获取   根据class
    def __init__(self,html):
        super(KKContentEnExt,self).__init__(html)
    
    def parse(self):
        lis = self.doc('#article_eng>div')
        content = ''
        for i in range(0,len(lis)):
            pq_li = pq(lis[i])
            content += str(pq_li.find('.qh_en').text())
        return content

class KKContentZgExt(KKBaseExtractor): # 中文获取   根据class
    def __init__(self,html):
        super(KKContentZgExt,self).__init__(html)
    
    def parse(self):
        lis = self.doc('#article_eng>div')
        for i in range(0,len(lis)):
            content = ''
            pq_li = pq(lis[i])
            content += str(pq_li.find('.qh_zg').text())
        return content

# 获取passage标题及其连接
psgDl = KKPsgDl(init_url='http://www.kekenet.com/read/news/keji')
html = psgDl.fetch_html()
psgExt = KKPsgExt(html)
psg_links = psgExt.parse()

# 获取psg文章内容并保存至total_content列表中
total_content = []
for link in psg_links:
    contentDl = ContentDl (init_url = link[1] )
    html = contentDl.fetch_html()
    conExtEn = KKContentEnExt(html)
    contenten = conExtEn.parse()
    conExtZh = KKContentZgExt(html)
    contentzh = conExtZh.parse()
    psg_link = link[1]
    psg_title = link[0]
    temp_dict = { 'title': psg_title, 'link': psg_link, 'en': str(contenten), 'zh': str(contentzh)}
    total_content.append(temp_dict)

# 将爬取内容写入文件中
with open('20191120week11练习1.txt', "w",encoding='utf-8') as f:
    json.dump(total_content, f,ensure_ascii=False)
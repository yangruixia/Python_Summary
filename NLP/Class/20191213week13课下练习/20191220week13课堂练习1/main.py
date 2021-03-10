
import lib
import pymongo
import json
import re
import pymysql
import time
import random
import threading

def InsertIntoMongodb(psg_link,col):
    for plink in psg_link:
        try:
            content = lib.GetContent(plink)
            if(content == ''):
                print('////Here//// Could not recognise!!!!!!!!!',plink)  
                continue
            else:
                col.insert_one(content)
                print('/////Here/////',plink)     
        except:
            continue     

if __name__ == "__main__":
    # 主函数
    # 1.首先获取所有导航栏链接  类似这样的：'http://www.kekenet.com/read/news'
    # 2.获取该专题下所有的文章页面，存储成为一个列表
    # 3.遍历导航连链接，判断是都在list1中，从而选取文章链接下载器
    #   list1 = ['图文', '时尚', '双语', '故事', '小说']    # h2中存在多个链接的页面标签
    # 4.遍历获取文章具体内容
    # ===============================================================================
    # 1.获取所有导航栏链接，存为一个list => nav
    nav = lib.GetNavLinks()
    # list如下
    # [('经验', 'http://www.kekenet.com/read/jy/'), ('图文', 'http://www.kekenet.com/read/pic/'), ('时尚', 'http://www.kekenet.com/read/ss/'), ('双语', 'http://www.kekenet.com/read/news/'), ('职场', 'http://www.kekenet.com/read/news/work/'), ('校园', 'http://www.kekenet.com/read/news/Economics/'), ('体育', 'http://www.kekenet.com/read/news/Sports/'), ('科技', 'http://www.kekenet.com/read/news/keji/'), ('时事', 'http://www.kekenet.com/read/news/politics/'), ('娱乐', 'http://www.kekenet.com/read/news/entertainment/'), ('经济', 'http://www.kekenet.com/read/news/economy/'), ('社会', 'http://www.kekenet.com/read/news/shehui/'), ('故事', 'http://www.kekenet.com/read/essay/'), ('小说', 'http://www.kekenet.com/read/story/'), ('海外', 'http://www.kekenet.com/read/culture/')]

    # 定义h2中有两个链接的标题
    list1 = ['图文', '时尚', '双语', '故事', '小说']
    # 遍历nav
    for n in nav:
        page_links = []      # 定义一个存放page link的列表
        page_links = lib.GetPageLinks(n) # 每一个nav下的列表，直接传递元组即可
    # 得到如下图所示的一个page links的列表，最后一个是一个元组，需要单独处理
    # ['http://www.kekenet.com/read/culture/List_1.shtml', 'http://www.kekenet.com/read/culture/List_2.shtml', 'http://www.kekenet.com/read/culture/List_3.shtml', 'http://www.kekenet.com/read/culture/List_4.shtml', 'http://www.kekenet.com/read/culture/List_5.shtml', 'http://www.kekenet.com/read/culture/List_6.shtml', 'http://www.kekenet.com/read/culture/List_7.shtml', 'http://www.kekenet.com/read/culture/List_8.shtml', 'http://www.kekenet.com/read/culture/List_9.shtml', 'http://www.kekenet.com/read/culture/List_10.shtml', 'http://www.kekenet.com/read/culture/List_11.shtml', 'http://www.kekenet.com/read/culture/List_12.shtml', 'http://www.kekenet.com/read/culture/List_13.shtml', 'http://www.kekenet.com/read/culture/List_14.shtml', 'http://www.kekenet.com/read/culture/List_15.shtml', 'http://www.kekenet.com/read/culture/List_16.shtml', 'http://www.kekenet.com/read/culture/List_17.shtml', 'http://www.kekenet.com/read/culture/List_18.shtml', 'http://www.kekenet.com/read/culture/List_19.shtml', 'http://www.kekenet.com/read/culture/List_20.shtml', 'http://www.kekenet.com/read/culture/List_21.shtml', 'http://www.kekenet.com/read/culture/List_22.shtml', 'http://www.kekenet.com/read/culture/List_23.shtml', 'http://www.kekenet.com/read/culture/List_24.shtml', 
    # 'http://www.kekenet.com/read/culture/List_25.shtml', 'http://www.kekenet.com/read/culture/List_26.shtml', 'http://www.kekenet.com/read/culture/List_27.shtml', 'http://www.kekenet.com/read/culture/List_28.shtml', 'http://www.kekenet.com/read/culture/List_29.shtml', 'http://www.kekenet.com/read/culture/List_30.shtml', 'http://www.kekenet.com/read/culture/List_31.shtml', 'http://www.kekenet.com/read/culture/List_32.shtml', 'http://www.kekenet.com/read/culture/List_33.shtml', 'http://www.kekenet.com/read/culture/List_34.shtml', 'http://www.kekenet.com/read/culture/List_35.shtml', 'http://www.kekenet.com/read/culture/List_36.shtml', 'http://www.kekenet.com/read/culture/List_37.shtml', 'http://www.kekenet.com/read/culture/List_38.shtml', 'http://www.kekenet.com/read/culture/List_39.shtml', 'http://www.kekenet.com/read/culture/List_40.shtml', ('海外', 'http://www.kekenet.com/read/culture/')]
    # 定义一个文章列表，用于保存文章列表
        main_link = page_links[len(page_links)-1]       # 获取主题  
        nav_name = main_link[0]
        client = pymongo.MongoClient('127.0.0.1',27017)
        db = client['kekenet']
        col = db[nav_name]
        if (main_link[0] in list1):                     # 判断主题是否在list1中   
            for i in range(0,len(page_links)-1):           # 除去最后一个，从前到后进行获取
                page_link = page_links[i]
                psg_link = lib.GetPsgLink1(page_link)
                if(psg_link == ''):
                    print('////////Something Wrong in extracting passage link!!!!///////')
                    continue
                else:
                    # InsertIntoMongodb(psg_link,col)
                    t = threading.Thread(target=InsertIntoMongodb, args=(psg_link,col))
                    t.start()

            psg_link = lib.GetPsgLink1(main_link[1]) 
            print('!!!!!!Last page!!!!!') 
            # InsertIntoMongodb(psg_link,col)        # 处理最后一个特殊链接          
            t = threading.Thread(target=InsertIntoMongodb, args=(psg_link,col))
            t.start()
        
        else:
            for i in range(0,len(page_links)-1):
                page_link = page_links[i]
                psg_link = lib.GetPsgLink2(page_link)
                if(psg_link == ''):
                    print('////////Something Wrong in extracting passage link!!!!///////')
                    continue
                else:
                    # InsertIntoMongodb(psg_link,col)
                    t = threading.Thread(target=InsertIntoMongodb, args=(psg_link,col))
                    t.start()
            psg_link = lib.GetPsgLink2(main_link[1]) 
            print('!!!!!Last oage!!!!!!')
            InsertIntoMongodb(psg_link,col)
            t = threading.Thread(target=InsertIntoMongodb, args=(psg_link,col))
            t.start()

        print('//////////////////////////////////////////////////////////////////////////////////////////////////////////')
        # print(psg_links)
        # 得到psg_links 结果如下
        # [{'title':"",'link':"",'time':"",'author':"",'tag':"",'en':"",'zh':""}]
        # 观察发现数据并不干净，但是中文和英文对应内容基本完整  
        # nav_name = main_link[0]
        # client = pymongo.MongoClient('127.0.0.1',27017)
        # db = client['kekenet']
        # col = db[nav_name]      
        # # 将该临时content存储进入mongo中
        # # 因为存储进入mongodb中会自动增加一个objectId字段，所以放在后面
        # # 计划将不同栏目中的数据存储进入不同的database中  
        # for layer1 in psg_links:        # 第一层遍历
        #     for plink in psg_link:
        #         try:
        #             content = lib.GetContent(plink)
        #             if(content == ''):
        #                 print('////Here//// Could not recognise!!!!!!!!!',plink)  
        #                 continue
        #             else:
        #                 col.insert_one(content)
        #                 print('/////Here/////',plink)     
        #         except:
        #              continue
        # print('///////////////////Have finished the'+ nav_name + ' content extraction/////////////////')   # 得到所有基本信息
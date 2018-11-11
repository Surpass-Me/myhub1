# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:57:17 2018

@author: tedu
"""

import requests
import re
import json
import time
from multiprocessing import Pool
from multiprocessing import Manager
import functools
# 抓取猫眼TOP100的数据

# 第一步： 下载页面
# 0-100： 0,10,20，...90
# https://maoyan.com/board/4?offset=90
def get_one_page(url):
    # 设置UA
    ua_header = {"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"}
    response = requests.get(url,headers=ua_header)
    if response.status_code == 200:
        return response.text
    else:
        return None
    
    
# 第二部： 提取信息
def parse_one_page(html):
    pattern = re.compile('<p class="name"[\s\S]*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    items = re.findall(pattern,html)
    
    for item in items:
        yield{
        "title":item[0].strip(),
        "actor":item[1].strip(),
        "time":item[2].strip()
        }
    
    
# 第三部： 保存到本地文件系统中
def write_to_file(item):
    with open("maoyanTop100.txt",'a',encoding="utf-8") as f:
        f.write(json.dumps(item,ensure_ascii=False))
        
def CrawlPage(offset):
    url = "https://maoyan.com/board/4?offset="
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)
    time.sleep(1)


if __name__ == "__main__":
    # 使用进程池来抓取数据
    pool = Pool()
    pool.map(CrawlPage,[i*10 for i in range(10)])
    pool.close()
    pool.join()
    
    
    
#    url = "https://maoyan.com/board/4?offset="
#    for i in range(0,100,10):
#        for item in parse_one_page(url+str(i)):
#            write_to_file(item)
            
















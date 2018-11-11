# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 18:43:12 2018

@author: tedu
"""
from bs4 import BeautifulSoup
from urllib import request

url1 = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id17"

fp = request.urlopen(url1)
soup = BeautifulSoup(fp.read())
polist = soup.findall("li")
print(polist[0].content[0])






























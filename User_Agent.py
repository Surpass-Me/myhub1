# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:04:02 2018

@author: tedu
"""

from urllib import request
import random


#headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

#作业：        
    #使用百度过来的user-agent大全，做一个UA(user-agent)池，对新浪的首页发起10次请求，
    #每次发起请求的UA需要随机从池中取出；

L = ["Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
     "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
     "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
     "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
     "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
     "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
     "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",
     "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser",
     "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
     "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)"
    ]
user_agent = random.choice(L)
headers = {"User-Agent":user_agent}
print(request.urlopen(
        request.Request('http://www.baidu.com',
                        headers=headers)
        ).read().decode("utf-8")
     )
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
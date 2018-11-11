# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 09:23:59 2018

@author: tedu
"""

import requests
import random

user_agent = ["Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
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

for _ in range(10):
    headers = {"User-Agent":random.choice(user_agent)}
    print(headers)
    response = requests.get("http://www.baidu.com",headers = headers)
    response.encoding = 'utf-8'
    print(response.status_code)
    print()
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 09:17:30 2018

@author: tarena
"""

import requests

#requests.get()
response = requests.get('http://www.baidu.com')
response.encoding = 'utf-8'
#print(response.status_code)
#print(response.content)
print(response.text)



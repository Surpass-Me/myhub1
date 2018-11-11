# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:09:37 2018

@author: tedu
"""

import re


rex = 'i=d%0A&from=AUTO&to=AUTO&smartresult=dict'
rex1 = re.sub(r'=',':',rex)
rex2 = re.sub(r'&','\n',rex1)
print(rex2)
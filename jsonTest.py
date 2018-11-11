# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 16:54:34 2018

@author: tedu
"""

import json

jsonDict = {"one":"1","two":"2"}
for key,value in jsonDict.items():
    print(key,value)
jsonDumps = json.dumps(jsonDict)  
print(jsonDumps)    # json encode
#   json -->  dict
jsonLoads = json.loads(jsonDumps)
for key in jsonLoads.keys():
    print(key)
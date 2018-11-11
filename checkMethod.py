# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 11:06:24 2018

@author: tedu
"""
import requests

def info(object, spacing=20, collapse=0):
    """
    遍历一遍Object对象，把里面可以被调用的方法及方法的doc string打印出来
    """
    # 第一步：提取出当前Object可以被调用的方法列表    
    methodList = [method for method in dir(object) if callable(getattr(object,method))]
    #print(methodList)
    
    #需要把doc string的方法按照一个的格式提取出来
    processFun = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)
    
    #打印出方法的名称及其文档的说明
    print('\n'.join(["%s %s"%( method.ljust(spacing), 
                    processFun(str(getattr(object,method).__doc__))) for method in methodList                
                    ])
        )
    
        
#def printInfo(s):
#    processFun = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)
#    return processFun


info(requests,collapse=1)
#s = 'str'
#info(s,collapse=1)
#print(printInfo(s.ljust.__doc__,1))


















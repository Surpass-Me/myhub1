# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:33:18 2018

@author: tedu
"""

def move(n,a,b,c):
    if n==1:
        return print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
        
move(3,'a','b','c')
print("hello everyone!")

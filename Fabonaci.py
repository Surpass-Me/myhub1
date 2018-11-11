# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 14:36:26 2018

@author: tedu
"""

#def Fab(n):
#    if n == 0 or n == 1:
#        return 1
#    return Fab(n-1)+Fab(n-2)


#def Fab2(n):
##    给斐波那契数列的前两个元素赋值
##    同时利用index记录循环进行的下标位置    
#    index, a, b = 0,1,1
#    while index <= n-2:
#        a, b = b, a+b
#        index += 1
#    return b
#
#for i in range(2):
#    print(Fab2(i))
    
    
    
def Fab3(n):
#    给斐波那契数列的前两个元素赋值
#    同时利用index记录循环进行的下标位置    
    index, a, b = 0,0,1
    while index <= n:
        yield b       #保留当前函数的上下文(变量及下一条)
        # 进入阻塞等待的状态
        a, b = b, a+b
        index += 1
    return b

if __name__ == "__main__":
    f = Fab3(7)
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    





























    
    
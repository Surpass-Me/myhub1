# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:37:04 2018

@author: tarena
"""
    
#哈希算法（对某段信息打指纹，能够压缩信息，HASH算法不可逆）
#HASH文件
import hashlib 

CHUNKSIZE = 4096
def hashFile(fileName):
    """
    对文件做hash    
    """
    h = hashlib.sha256()
    with open(fileName,'rb') as f:
        while True:
            chunk = f.read(CHUNKSIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()    #得到文件最终的hash值


  
# hash某个字符串
def hashStr(strInfo):
    h = hashlib.md5()
    h.update((strInfo).encode('utf-8'))
    return h.hexdigest()

if __name__ == "__main__":
    print(hashStr('hello world'))
    print(hashStr('hello world1'))
    
    print(hashFile('note'))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
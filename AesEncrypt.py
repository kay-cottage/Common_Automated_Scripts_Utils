# -*- coding: utf-8 -*-
"""
Created on Tue Feb.1 09:12:41 2022
@author: gw.kayak
"""
from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
from Crypto import Random
import base64
import os
import time
from batch import batch


class AesEncrypt(object):
    def __init__(self, key, mode=AES.MODE_CFB):
        self.key = self.check_key(key)
        # 密钥key长度必须为16,24或者32bytes的长度
        self.mode = mode
        self.iv = b'7#7FqXu\x06\x847-\xba\xe5\x07\xeb\xa7'
        #self.iv = Random.new().read(AES.block_size)
        print(self.iv)

    def check_key(self, key):
        '检测key的长度是否为16,24或者32bytes的长度'
        try:
            if isinstance(key, bytes):
                assert len(key) in [16, 24, 32]
                return key
            elif isinstance(key, str):
                assert len(key.encode()) in [16, 24, 32]
                return key.encode()
            else:
                raise Exception(f'密钥必须为str或bytes,不能为{type(key)}')
        except AssertionError:
            print('输入的长度不正确')

    def check_data(self,data):
        '检测加密的数据类型'
        if isinstance(data, str):
            data = data.encode()
        elif isinstance(data, bytes):
            pass
        else:
            raise Exception(f'加密的数据必须为str或bytes,不能为{type(data)}')
        return data
    def encrypt(self, data):
        ' 加密函数 '
        data = self.check_data(data)
        cryptor = AES.new(self.key, self.mode,self.iv)
        return b2a_hex(cryptor.encrypt(data)).decode()

    def decrypt(self,data):
        ' 解密函数 '
        data = self.check_data(data)
        cryptor = AES.new(self.key, self.mode,self.iv)
        return cryptor.decrypt(a2b_hex(data)).decode()




    def encrypt_file(self,dir_file_list):
        count = 0
        for name in dir_file_list:
                with open(name,"rb") as f:
                    base64_data = base64.b64encode(f.read())
                    data = base64_data
                with open(name,"w") as f:
                    e = self.encrypt(data)
                    f.write(e)
                    f.close()
                count = count+1
        print('（encrypr successfully)共成功加密'+str(count)+'个文件')            


    def decrypt_file(self,dir_file_list):
        count = 0
        for name in dir_file_list:
                with open(name,"rb") as f:
                    d = self.decrypt(f.read())                
                    base64_data = base64.b64decode(d)
                    data = base64_data
                with open(name,"wb") as f:
                    f.write(data)
                    f.close()
                count = count+1
        print('（decrypr successfully)共成功解密'+str(count)+'个文件')  






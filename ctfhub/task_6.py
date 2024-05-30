#!C:\Python3.7
# -*- coding:utf-8 -*-
from jwt import PyJWT
import string
import itertools

def brute_HS256(encode):
    keys = string.ascii_lowercase
    # print(keys)
    for i in itertools.product(keys, repeat=4):
        key = "".join(i)
        print("[--]test ", key)
        try:
            print("[****]key:", key, PyJWT.decode(encode, key, algorithms="HS256"))
            break
        except Exception as e:
            pass
        print(key)


if __name__ == '__main__':
    encode = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxMjM0NTYiLCJyb2xlIjoiZ3Vlc3QifQ.uTksRlcqXLjk_n-XbObBH9jgULQ5MxE2H2eGJXX7UKs"
    brute_HS256(encode)

# encoding: utf-8
"""
@version: python3.6
@author: ‘eric‘
@license: Apache Licence 
@contact: steinven@qq.com
@site: 00123.ml:8000
@software: PyCharm
@file: utils.py
@time: 2018/6/20 4:49
"""
import configparser,requests
from http.cookies import SimpleCookie
import pickle, os
from lxml import etree
cf = configparser.ConfigParser()
cf.read('conf.ini')


def get_config(key):
    return cf.get('default',key)


def set_config(key,value):
    cf.set('default',key,value)
    cf.write(open('conf.ini', 'w'))

def serialize_cookie(cookie):
    with open('cookie', 'wb') as f:
        pickle.dump({k.key: k.value for k in SimpleCookie(cookie).values()}, f)

def deserialize_cookie():
    try:
        with open('cookie', 'rb') as f:
            return pickle.load(f)
    except:
        set_config('islogin','')



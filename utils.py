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
import configparser
cf = configparser.ConfigParser()
cf.read('temp.ini')
def get_config(key):
    return cf.get('default',key)
def set_config(key,value):
    cf.set('default',key,value)
    cf.write(open('temp.ini', 'w'))

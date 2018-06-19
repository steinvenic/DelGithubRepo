# encoding: utf-8
"""
@version: python3.6
@author: ‘eric‘
@license: Apache Licence 
@contact: steinven@qq.com
@site: 00123.ml:8000
@software: PyCharm
@file: demo.py
@time: 2018/6/16 21:44
"""

import requests
from lxml import etree
from utils import *
base_url = 'https://github.com/'


def get_authenticity_token():
  headers = {
        "Host": "github.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
  r = requests.get(url=base_url+'login',headers=headers,verify=False)
  cookie = r.cookies
  respose_etree = etree.HTML(r.text);
  authenticity_token = respose_etree.xpath('//input[@name="authenticity_token"]/@value')
  set_config('authenticity_token',authenticity_token[0])
  return  cookie

def login():
  cookie = get_authenticity_token()
  headers = {
  "Host": "github.com",
  "Connection": "keep-alive",
  "Content-Length": "188",
  "Cache-Control": "max-age=0",
  "Origin": "https://github.com",
  "Upgrade-Insecure-Requests": "1",
  "Content-Type": "application/x-www-form-urlencoded",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
  "Referer": "https://github.com/login",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "zh-CN,zh;q=0.9",
}
  data = {
  "commit": "Sign in",
  "utf8": "✓",
  "authenticity_token": "Wv4tx8UGR2B6pt1InJiLQ1AEVJMouNn0C/FMW4LJk8JdZn2wx4kIxw805mSTw0OauVC/nuF0dfR7AIpk6qd7HA==",
  "login": "761701732@qq.com",
  "password": "aaa00123"
}
  data.update({"authenticity_token": get_config('authenticity_token')})
  cookie = requests.post(base_url+'session',headers=headers,data=data,verify=False,cookies=cookie).cookies
  return cookie

def get_new_auth():
  cookie = login()
  headers = {
  "Host": "github.com",
  "Connection": "keep-alive",
  "Accept": "text/html",
  "X-Requested-With": "XMLHttpRequest",
  "X-PJAX": "true",
  "X-PJAX-Container": "#js-repo-pjax-container",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
  "Referer": "https://github.com/steinvenic/toupiao",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "zh-CN,zh;q=0.9",
}
  url = 'https://github.com/steinvenic/LZUthesis/settings'
  params = {
  "_pjax": "%23js-repo-pjax-container"
}
  r = requests.get(url,headers=headers,params=params,cookies=cookie,verify=False)
  html = etree.HTML(r.text)
  authenticity_token = html.xpath('//form[contains(@action,"delete")]//input[@name="authenticity_token"]/@value')
  return cookie,authenticity_token

def delete_repo():
  d = get_new_auth()
  headers = {
  "Host": "github.com",
  "Connection": "keep-alive",
  "Content-Length": "156",
  "Cache-Control": "max-age=0",
  "Origin": "https://github.com",
  "Upgrade-Insecure-Requests": "1",
  "Content-Type": "application/x-www-form-urlencoded",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
  "Referer": "https://github.com/steinvenic/toupiao/settings",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "zh-CN,zh;q=0.9",
}
  data = {
    "utf8": "✓",
    "_method": "delete",
    "authenticity_token": "VdeGKzd97V1w6oquFN7JmKU4Ylhkeq9CqwVzpQ8uD8yNnHBax9dmvoyaOr0sBIU5qZVpSIIr7cOGSz0A57F7KQ==",
    "verify": "LZUthesis"
  }
  data.update({"authenticity_token":d[1]})
  url = 'https://github.com/steinvenic/LZUthesis/settings/delete'
  r = requests.post(url,headers=headers,cookies=d[0],data=data,verify=False)

delete_repo()






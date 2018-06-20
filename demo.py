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

import requests,click,logging
import sys
from lxml import etree
from utils import *
base_url = 'https://github.com/'
headers = {
    "Host": "github.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}



def get_authenticity_token():

    r = requests.get(url=base_url+'login',headers=headers,verify=False)
    cookie = r.cookies
    respose_etree = etree.HTML(r.text);
    authenticity_token = respose_etree.xpath('//input[@name="authenticity_token"]/@value')
    set_config('authenticity_token',authenticity_token[0])
    return  cookie

def login():
      cookie = get_authenticity_token()
      data = {
      "commit": "Sign in",
      "utf8": "✓",
    }
      data.update({"authenticity_token": get_config('authenticity_token'),
                   "login": get_config('user_name'),
                   "password": get_config('password'),
                   })
      r = requests.post(base_url+'session',headers=headers,data=data,verify=False,cookies=cookie)
      respose_etree = etree.HTML(r.text);
      nick_name = respose_etree.xpath('//meta[@name="octolytics-actor-login"]/@content')
      set_config('nick_name',nick_name[0])
      cookie = r.cookies
      return cookie

def get_new_auth():
      cookie = login()
      url = base_url+ get_config('nick_name') + '/' +get_config('repo_name') + '/settings'
      params = {
      "_pjax": "%23js-repo-pjax-container"
    }
      r = requests.get(url,headers=headers,params=params,cookies=cookie,verify=False)
      html = etree.HTML(r.text)
      authenticity_token = html.xpath('//form[contains(@action,"delete")]//input[@name="authenticity_token"]/@value')
      return cookie,authenticity_token

def delete_repo():
      d = get_new_auth()
      data = {
        "utf8": "✓",
        "_method": "delete",
      }
      data.update({"authenticity_token":d[1],
                   "verify": get_config('repo_name'),
                   })
      url = base_url + get_config('nick_name') + '/' + get_config('repo_name') + '/settings/delete'
      requests.post(url,headers=headers,cookies=d[0],data=data,verify=False)


def del_target(repo_name):
    set_config('repo_name',repo_name)
    delete_repo()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    repo_list = sys.argv[1:]
    logging.info(repo_list)
    for i in repo_list:
        del_target(i)










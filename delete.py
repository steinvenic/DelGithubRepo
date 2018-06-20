# encoding: utf-8
"""
@version: python3.6
@author: ‘eric‘
@license: Apache Licence 
@contact: steinven@qq.com
@site: 00123.ml:8000
@software: PyCharm
@file: delete.py
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
#Remove SSL warning
requests.packages.urllib3.disable_warnings()


def get_cookie():
    r = requests.get(url=base_url+'login',headers=headers,verify=False)
    cookie = r.cookies
    respose_etree = etree.HTML(r.text);

    # Get authenticity_token By xpath
    authenticity_token = respose_etree.xpath('//input[@name="authenticity_token"]/@value')
    set_config('authenticity_token',authenticity_token[0])
    logging.info('已获取authenticity_token')
    return  cookie


def login():
    cookie = get_cookie()
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
    #获取用户名
    nick_name = respose_etree.xpath('//meta[@name="octolytics-actor-login"]/@content')
    if len(nick_name) > 0:
        set_config('nick_name',nick_name[0])
        cookie = r.cookies
        logging.info('登陆成功！')
    else:
        logging.info('登陆失败，请检查配置文件【conf.ini】用户名和密码！')
        sys.exit(1)
    return cookie


def get_authenticity_token():
    cookie = login()
    url = base_url+ get_config('nick_name') + '/' +get_config('repo_name') + '/settings'
    params = {
      "_pjax": "%23js-repo-pjax-container"
    }
    r = requests.get(url,headers=headers,params=params,cookies=cookie,verify=False)
    html = etree.HTML(r.text)
    authenticity_token = html.xpath('//form[contains(@action,"delete")]//input[@name="authenticity_token"]/@value')
    logging.info('获取authenticity_token成功！')
    return cookie,authenticity_token


def delete_repo():
    logging.info('正在删除%s' %get_config('repo_name'))
    d = get_authenticity_token()
    data = {
    "utf8": "✓",
    "_method": "delete",
    }
    data.update({"authenticity_token":d[1],
               "verify": get_config('repo_name'),
               })
    url = base_url + get_config('nick_name') + '/' + get_config('repo_name') + '/settings/delete'
    r = requests.post(url,headers=headers,cookies=d[0],data=data,verify=False)
    if r.status_code !=200:
      logging.info('*'*20+'删除【%s】失败' % get_config('repo_name')+'*'*20)
      sys.exit(1)
    logging.info('*'*20+'删除[%s]成功' % get_config('repo_name') +'*'*20)


def del_target(repo_name):
    set_config('repo_name',repo_name)
    delete_repo()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    repo_list = sys.argv[1:]
    for i in repo_list:
        del_target(i)












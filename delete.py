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
from http import cookiejar

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
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def get_cookie():
    r = requests.get(url=base_url+'login',headers=headers,verify=False)
    cookie = r.cookies
    respose_etree = etree.HTML(r.text);
    # Get authenticity_token By xpath
    authenticity_token = respose_etree.xpath('//input[@name="authenticity_token"]/@value')
    set_config('authenticity_token',authenticity_token[0])
    logging.info('已获取authenticity_token')
    serialize_cookie(cookie)


def login():

    cookie =deserialize_cookie()
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
        cookie1 = r.cookies
        logging.info('登陆成功！')
    else:
        logging.info('登陆失败，请检查配置文件【conf.ini】用户名和密码！')
        set_config('isLogin','False')
    serialize_cookie(cookie1)


def get_authenticity_token():
    cookie = deserialize_cookie()
    url = base_url+ get_config('nick_name') + '/' +get_config('repo_name') + '/settings'
    params = {
      "_pjax": "%23js-repo-pjax-container"
    }
    r = requests.get(url,headers=headers,params=params,cookies=cookie,verify=False)
    html = etree.HTML(r.text)
    authenticity_token = html.xpath('//form[contains(@action,"delete")]//input[@name="authenticity_token"]/@value')
    logging.info('获取authenticity_token成功！')
    serialize_cookie(cookie)
    set_config('isLogin', 'True')
    return authenticity_token


def delete_repo():
    logging.info('正在删除%s' %get_config('repo_name'))
    data = {
    "utf8": "✓",
    "_method": "delete",
    }
    data.update({"authenticity_token":get_authenticity_token(),
               "verify": get_config('repo_name'),
               })
    url = base_url + get_config('nick_name') + '/' + get_config('repo_name') + '/settings/delete'
    r = requests.post(url,headers=headers,cookies=deserialize_cookie(),data=data,verify=False)
    if r.status_code !=200:
      logging.info('*'*20+'删除【%s】失败' % get_config('repo_name')+'*'*20)
      sys.exit(1)
    logging.info('*'*20+'删除[%s]成功' % get_config('repo_name') +'*'*20)


def get_repo_list(page):
    url = 'https://github.com/'+ get_config('nick_name')
    params = {
    "page": page,
    "tab": "repositories"
}
    get_cookie()
    login()
    raw_html = requests.get(url,params,cookies=deserialize_cookie(),headers=headers,verify=False).text
    e_html = etree.HTML(raw_html)
    repo_list = e_html.xpath('//ul/li//a[@itemprop="name codeRepository"]/text()')
    re_repo_list = [x.strip() for x in repo_list]
    repo_nums = e_html.xpath('//a[@title="Repositories"]/span/text()')[0]
    return re_repo_list,repo_nums

def get_all_repo_list():
    d = get_repo_list(1)
    all_repo_list = d[0]
    repo_nums = int(d[1])
    if repo_nums < 31:
        return  all_repo_list
    else:
        pages = repo_nums//30 + 1
        for i in range(2,pages+1):
            all_repo_list += get_repo_list(i)[0]
        return all_repo_list


def del_target(repo_name):
    set_config('repo_name', repo_name)
    if get_config('isLogin')=='False':
        get_cookie()
        login()
        get_authenticity_token()
    delete_repo()


print(get_all_repo_list())
# if __name__ == '__main__':
#
#     repo_list = sys.argv[1:]
#     for i in repo_list:
#         del_target(i)
#     set_config('isLogin','False')














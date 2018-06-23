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
import prettytable as pt
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
    '''
    获取登录界面authenticity_token、保存cookie
    :return: None
    '''
    r = requests.get(url=base_url+'login',headers=headers,verify=False)
    cookie = r.cookies
    respose_etree = etree.HTML(r.text);
    # Get authenticity_token By xpath
    authenticity_token = respose_etree.xpath('//input[@name="authenticity_token"]/@value')
    set_config('authenticity_token',authenticity_token[0])
    logging.info('已获取登录页authenticity_token')
    serialize_cookie(cookie)


def login():
    '''
    登录，获取用户名、保存cookie
    :return:
    '''
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
        cookie = r.cookies
        logging.info('登陆成功！')
        set_config('isLogin', 'True')
    else:
        logging.info('登陆失败，请检查配置文件【conf.ini】用户名和密码！')
        set_config('isLogin','False')
    serialize_cookie(cookie)


def get_authenticity_token():
    '''
    获取
    :return:
    '''
    cookie = deserialize_cookie()
    url = base_url+ get_config('nick_name') + '/' +get_config('repo_name') + '/settings'
    params = {
      "_pjax": "%23js-repo-pjax-container"
    }
    r = requests.get(url,headers=headers,params=params,cookies=cookie,verify=False)
    html = etree.HTML(r.text)
    authenticity_token = html.xpath('//form[contains(@action,"delete")]//input[@name="authenticity_token"]/@value')
    logging.info('获取被删authenticity_token成功！')
    serialize_cookie(cookie)
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
    logging.info('*'*20+'删除【%s】成功' % get_config('repo_name') +'*'*20)


def get_repo_list(page):
    url = 'https://github.com/'+ get_config('nick_name')
    params = {
    "page": page,
    "tab": "repositories"
}

    raw_html = requests.get(url,params,cookies=deserialize_cookie(),headers=headers,verify=False)
    if raw_html.status_code !=200 or get_config('isLogin')=='False' or get_config('isLogin')=='':
        get_cookie()
        login()
        url = 'https://github.com/' + get_config('nick_name')
        raw_html = requests.get(url, params, cookies=deserialize_cookie(), headers=headers, verify=False)
    e_html = etree.HTML(raw_html.text)
    repo_list = e_html.xpath('//ul/li//a[@itemprop="name codeRepository"]/text()')
    re_repo_list = [x.strip() for x in repo_list]
    repo_nums = e_html.xpath('//a[@title="Repositories"]/span/text()')[0]
    return re_repo_list,repo_nums

def get_all_repo_list():
    if get_config('isLogin')=='False'  or get_config('isLogin')=='':
        get_cookie()
        login()
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




def repo_table_list(flag):
    repo_list = get_all_repo_list()
    list_len = len(repo_list)
    tb = pt.PrettyTable()
    tb.field_names = ['ID_1', 'RepoName_1', 'ID_2', 'RepoName_2']
    for i in range(0, list_len - 1, 2):
        tb.add_row([i, repo_list[i], i + 1, repo_list[i + 1]])
    if list_len % 2 == 1:
        tb.add_row([list_len - 1, repo_list[-1], '*', '*'])
    if flag == 'true':
        print(tb)
    return repo_list


def del_target(repo_name):
    set_config('repo_name', repo_name)
    if get_config('isLogin')=='False'  or get_config('isLogin')=='':
        get_cookie()
        login()
        get_authenticity_token()
    delete_repo()


if __name__ == '__main__':
    option = sys.argv[1]
    if option == '-list':
        repo_table_list('true')
    elif option == '-name':
        repo_list = sys.argv[2:]
        confirm_status = input('确认删除%s？,按y确认' % str(repo_list))
        if confirm_status == 'y':
            set_config('pre_del',str(repo_list))
            logging.info(repo_list)
            for i in repo_list:
                del_target(i)

    elif option == '-id':
        pre_del_list = []
        repo_id_list = sys.argv[2:]
        repo_list = repo_table_list('false')
        for pre_del in repo_id_list:
            pre_del_list.append(repo_list[int(pre_del)])

        confirm_status = input('确认删除%s？,按y确认' % str(pre_del_list))
        if confirm_status == 'y':
            set_config('pre_del',str(pre_del_list))
            logging.info(repo_id_list)
            for i in pre_del_list:
                del_target(i)

    elif option == '-all':

        repo_list = repo_table_list('false')


        confirm_status = input('确认删除所有项目？？？？%s,按y确认' % str(repo_list))
        if confirm_status == 'y':
            set_config('pre_del',str(repo_list))
            logging.info(repo_list)
            for i in repo_list:
                del_target(i)
















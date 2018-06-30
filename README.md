# 思路
* Fiddler抓包获取登录、项目列表、删除等操作的请求
* 使用xpath获取相关token和用户名等参数，pickle模块序列化cookie
* prettytable 打印输出

# 安装 
* Python3.6
* `pip install -r requirements.txt`
*  没有Python环境，请使用[Release](https://github.com/steinvenic/DelGithubRepo/releases)

#  用法

* 修改配置文件conf.ini，改成自己的账号和密码,`isLogin`不要填写，如果更改账号，一定要清空`isLogin`！  
* `python delete.py -ls`    ====>显示项目列表
* `python delete.py -name test1 test2`    ====>删除test1 test2两个项目
* `python delete.py -id 0 1`              ====>删除ID 0、1对应的项目,请仔细确认被删除的项目名称！
![avartar](https://github.com/steinvenic/DelGithubRepo/blob/master/20180624002334.png)

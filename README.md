# 思路
* Fiddler抓包获取登录、项目列表、删除等操作的请求
* 使用xpath获取相关token和用户名等参数，pickle模块序列化cookie
* prettytable 打印输出

# 安装 
* Python3.6
* `pip install -r requirements.txt`
*  没有Python环境，请使用[Release](https://github.com/steinvenic/DelGithubRepo/releases)
*  提供[百度云下载](https://pan.baidu.com/s/1hy59KV_nHQtn1Ogd0E1hdg)，密码`6ufa`

#  使用

* 修改配置文件conf.ini，改成自己的账号和密码,`isLogin`的值不要填写
* 如果更换账号，一定要清空`isLogin`的值，或改为False！
## 示例：
* `delete.exe -h`    ====>显示帮助页面
* `delete.exe -ls`    ====>显示所有项目列表
* `delete.exe -name test1 test2`    ====>删除test1 test2两个项目
* `delete.exe -id 0 1`              ====>删除ID 0、1对应的项目,请仔细确认被删除的项目名称！
* `delete.exe -fork`    ====>删除所有Fork的项目
* `delete.exe -all`    ====>删除所有项目
![avartar](https://github.com/steinvenic/DelGithubRepo/blob/master/20180624002334.png)

#  问题
若执行中报错，请修改配置文件中isLogin的值为False，不能解决请提Issue

# gsdata-python-sdk

![MIT](https://img.shields.io/npm/l/express.svg) [![version](https://img.shields.io/pypi/v/gsdata.svg)](https://pypi.python.org/pypi/gsdata)  [![Build Status](https://travis-ci.org/superalsrk/gsdata-python-sdk.svg?branch=master&v=11)](https://travis-ci.org/superalsrk/gsdata-python-sdk)


### 前言

[gsdata-python-sdk](http://github.com/superalsrk/gsdata-python-sdk) 是一个非官方的 [gsdata](http://open.gsdata.cn/) python开发包, 祝使用愉快。

+ [issure地址](https://github.com/superalsrk/gsdata-python-sdk)
+ 支持 python2.6, python2.7, python3.2, python3.3, python3.4, python3.5

### 安装

```bash
$ pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com gsdata
```

### 使用

```python

from gsdata import Gsdata

#创建客户端
client = Gsdata("YOUR_APP_ID", "YOUR_APP_SECRET")

#获取用户信息
ret1 = client.sys_user_info('saber@stackbox.org')

#用户名验证
ret2 = client.sys_check_user('saber@stackbox.org')

#其他API, 第一个参数为API地址, 第二个参数为请求参数字典(除去appid和appkey)
ret3 = client.call('/api/wx/wxapi/wx_content', {'url':'http://mp.weixin.qq.com/s?__biz=MzAxOTEyMDI1MQ==&mid=400950548&idx=3&sn=cca852f541f93c53633a4e0069230313&3rd=MzA3MDU4NTYzMw==&scene=6#rd'})
		
```




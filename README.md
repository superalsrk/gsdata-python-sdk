# gsdata-python-sdk

![MIT](https://img.shields.io/npm/l/express.svg)  [![Build Status](https://travis-ci.org/superalsrk/gsdata-python-sdk.svg?branch=master&v=9)](https://travis-ci.org/superalsrk/gsdata-python-sdk)


### 前言

[gsdata-python-sdk](http://github.com/superalsrk/gsdata-python-sdk) 是一个非官方的gsdata python开发包, 祝使用愉快。

+ [issure地址](https://github.com/superalsrk/gsdata-python-sdk)
+ 支持 python2.6, python2.7, python3.3, python3.4, python3.5

### 安装

```bash
$ pip install gsdata

//或者

$ easy_install gsdata
```

### 使用

```python

from gsdata import Gsdata

client = Gsdata("YOUR_APP_ID", "YOUR_APP_SECRET")

#获取用户信息
ret1 = client.sys_user_info('saber@stackbox.org')

#用户名验证
ret2 = client.sys_check_user('saber@stackbox.org')

#其他API, 第一个参数为API地址, 第二个参数为请求参数字典(除去appid和appkey)
t = client.call('/api/wx/wxapi/wx_content', {'url':'http://mp.weixin.qq.com/s?__biz=MzAxOTEyMDI1MQ==&mid=400950548&idx=3&sn=cca852f541f93c53633a4e0069230313&3rd=MzA3MDU4NTYzMw==&scene=6#rd'})
		
```




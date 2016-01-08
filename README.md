# gsdata-python-sdk

![MIT](https://img.shields.io/npm/l/express.svg)  [![Build Status](https://travis-ci.org/superalsrk/gsdata-python-sdk.svg?branch=master)](https://travis-ci.org/superalsrk/gsdata-python-sdk)


### 前言

[gsdata-python-sdk](http://github.com/superalsrk/gsdata-python-sdk) 是一个非官方的gsdata python开发包, 祝使用愉快。
+ [项目地址](https://github.com/superalsrk/gsdata-python-sdk)
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

client = Gsdata(app_id = "YOUR_APP_ID", app_secret = "YOUR_APP_SECRET")
params = {'id' : 3535, 'biz' : 'TESTBIZ'}

result = client.execute('http://testurl.com', body = params)
```

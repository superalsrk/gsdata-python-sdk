# -*- coding: utf-8 -*-

import requests
import json
import base64
from .signature import Signature

class Gsdata:
	def __init__(self, appid, appkey):
		self.appid = appid
		self.appkey = appkey
		self.__class__.host = 'http://open.gsdata.cn'

	def sys_user_info(self, loginname):
		params = dict()
		params['loginname'] = loginname
		return self.call('/api/sys/sysapi/user_info', params)

	def sys_check_user(self, loginname):
		params = dict()
		params['loginname'] = loginname
		return self.call('/api/sys/sysapi/check_user', params)


	def call(self, api, params):
		params['appid'] = self.appid
		params['signature'] = Signature.md5(Signature.sort_json(params).lower() + self.appkey)
		params_json = json.dumps(params, separators=(',', ':'))

		return requests.post(self.__class__.host + api,
						headers = {'Content-Type': 'application/octet-stream'},
						data = base64.encodestring(params_json.encode('utf-8'))).text
	@property
	@classmethod
	def host(cls):
		return cls.host

	@host.setter
	def host(cls, value):
		cls.host = value
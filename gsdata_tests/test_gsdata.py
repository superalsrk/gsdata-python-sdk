# -*- coding: utf-8 -*-

import unittest
import json
from gsdata import Signature
from gsdata import Gsdata


class TestGsdata(unittest.TestCase):
	def test_md5(self):
		assert Signature.md5('{"appid":"xto3s5r4utwlloii2aa0","loginname":"saber@stackbox.org"}94GSwqAL2PwdPbM9N02KNHuf9') == 'f91e20ab7736cd33ed312e1fb0ab8d98'

	def test_sort_json(self):
		test_params = {'loginname': 'saber@stackbox.org', 'appid':'xto3s5r4utwlloii2aa0'}
		assert Signature.sort_json(test_params) == '{"appid":"xto3s5r4utwlloii2aa0","loginname":"saber@stackbox.org"}'

	def test_gsdata_host(self):
		client = Gsdata('XtO3S5r4uTWLLoiI2Aa0','94GSwqAL2PwdPbM9N02KNHuf9')
		assert Gsdata.host == 'http://open.gsdata.cn'
		Gsdata.host = 'http://demo.cn'
		assert Gsdata.host == 'http://demo.cn'

	def test_sys_user_info(self):
		client = Gsdata('XtO3S5r4uTWLLoiI2Aa0','94GSwqAL2PwdPbM9N02KNHuf9')
		t = client.sys_user_info('saber@stackbox.org')
		assert json.loads(t).get('returnCode') == '1001'

	def test_sys_check_user(self):
		client = Gsdata('XtO3S5r4uTWLLoiI2Aa0','94GSwqAL2PwdPbM9N02KNHuf9')
		t = client.sys_check_user('saber@stackbox.org')
		assert json.loads(t).get('returnCode') == '1001'

	def test_normal(self):
		client = Gsdata('XtO3S5r4uTWLLoiI2Aa0','94GSwqAL2PwdPbM9N02KNHuf9')
		t = client.call('/api/wx/wxapi/wx_content', {'url':'http://mp.weixin.qq.com/s?__biz=MzAxOTEyMDI1MQ==&mid=400950548&idx=3&sn=cca852f541f93c53633a4e0069230313&3rd=MzA3MDU4NTYzMw==&scene=6#rd'})
		assert json.loads(t).get('returnCode') == '1001'

if __name__ == '__main__':
    unittest.main()


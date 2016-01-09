# -*- coding: utf-8 -*-

from collections import OrderedDict
import hashlib
import json

class Signature:
	@classmethod
	def md5(cls, src):
		return hashlib.md5(src.encode()).hexdigest()

	@classmethod
	def sort_json(cls, params):
		sort_tuples = OrderedDict(sorted(params.items(), key=lambda t: t[0]))
		return json.dumps(sort_tuples,separators=(',', ':'))

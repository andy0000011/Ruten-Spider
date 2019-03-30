# -*- coding: UTF-8 -*-
import requests
import json
from bs4 import BeautifulSoup
import re

class Net:
	def __init__(self):
		pass

	def get_response(self, url, page=1):
		headers = {	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",}
		params = {"p": page}
		response = requests.get(url, headers=headers, params=params)
		
		return response

	def get_json(self, search_word, text):
		try:
			res_json = re.search(search_word, text).group(1)
		except:
			res_json = "error"
		
		return res_json
	
if __name__ == "__main__":
	net = Net()
	url = "https://class.ruten.com.tw/user/index00.php?s=hambergurs"
	r = net.get_response(url)
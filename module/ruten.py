# -*- coding: UTF-8 -*-
import net
import requests
import json
from bs4 import BeautifulSoup
import re

class Ruten:
	def __init__(self):
		self.Net = net.Net()
		
	def get_shop(self, url, page):
		link = []
		for i in range(page):
			params = {"p": page}
			r = self.Net.get_response(url, page)
			soup = BeautifulSoup(r.content.decode(), "lxml")
			products = soup.find_all("div", class_="rt-store-goods-disp-mix")
			product_link = []
			
			for j in products:
				product_link.append(j.find("h3").find("a")["href"])
			link.append(product_link)
		
		return product_link
		
	def get_product(self, url_list):
		dict = {"SEVEN_COD": "7-11取貨付款",
		"CVS_COD": "全家、OK、萊爾富取貨付款", 
		"MAPLE": "便利帶隔日配", 
		"SEVEN": "7-11取貨", 
		"POST": "郵寄寄送", 
		"HOUSE": "宅配/快遞", 
		"ISLAND": "離島寄送"}
		data = []
		print("取得資料中，請稍後...")
		for i in range(len(url_list)):
			temp = {}
			product_url = url_list[i]
			product_res = self.Net.get_response(product_url).content.decode()
			result = self.Net.get_json("RT\.context =(.+);", product_res)
			result = json.loads(result)
			temp["name"] = result["item"]["name"]
			temp["image"] = result["item"]["images"][0]["original"]
			temp["shipment"] = {}
			for j in result["item"]["shipment"]:
				j["name"] = dict[j["name"]]
			temp["shipment"] = result["item"]["shipment"]
	
			data.append(temp)
		data = json.dumps(data)
		print(data)
		
		return data
		
if __name__ == "__main__":
	ruten = Ruten()
	url = "https://class.ruten.com.tw/user/index00.php?s=hambergurs"
	for i in range(3):
		products_link = ruten.get_shop(url, i+1)
		ruten.get_product(products_link)

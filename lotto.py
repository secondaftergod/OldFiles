import requests
import bs4
from collections import Counter
import copy
import pprint
import random

Url='https://www.multilotto.com/en/lotto-results/israel-lotto'

result=[]

stat=[]

sorter_stat=[]

def get_html(Url):
	r=requests.get(Url)
	return r
	
def get_content(html):
	soup=bs4.BeautifulSoup(html, "html.parser")
	items=soup.find_all('div',class_="prize-number")
	for i in items:
		chusla=i.get_text()
		result.append(chusla)
	
def rozigrash(html):
	soup=bs4.BeautifulSoup(html, "html.parser")
	itemall=soup.find_all('a',class_="btn big blue fleft")
	for i in itemall:
		newurl=i.get('href')
	def get_html2(newurl):
		a=requests.get(newurl)
		return a
	try:
		html2=get_html(newurl)
	except UnboundLocalError:
		print('Статистика:')
		print(str(len(result)/6),' Розіграшів')
		print('')
		global stat
		for i in range(4):
			random.shuffle(stat)
			
			print(stat[0:6])
		stat=dict(Counter(stat))
		print('')
		sorter_stat=sorted(stat.items(),key=lambda x:x[1])
		for i in sorter_stat:
			print('Число ',i[0],'::',i[1],' Разів')
	get_content2(html2.text)
	rozigrash(html2.text)

def get_content2(html2):
	soup=bs4.BeautifulSoup(html2, "html.parser")
	items=soup.find_all('div',class_="prize-number")
	for i in items:
		chusla=i.get_text()
		result.append(chusla)
		stat.append(chusla)
		

def parse():
	html=get_html(Url)
	if html.status_code==200:
			get_content(html.text)
			rozigrash(html.text)
	else:
		print('error')
		
parse()


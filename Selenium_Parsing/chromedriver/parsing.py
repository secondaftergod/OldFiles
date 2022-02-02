import requests
import bs4
#Парсинг----------------------
Url='https://learn.skillup.ua/room/intqa_wb1?username=lox&email=soba%40ma.ru&phone=%2B380546464848&autologin=1&lead=7736ed42-e6be-4928-befc-b91292de78bb'
headers={"User-Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1'}
r=requests.get(Url,headers=headers)

soup=bs4.BeautifulSoup(r.content,"html.parser")
items=soup.find_all('input',placeholder="")



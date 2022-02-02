import requests
import bs4
#Парсинг----------------------
Url='https://bidfax.info/tesla/model-y/'
headers={"User-Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1'}
r=requests.get(Url,headers=headers)
print(r)
soup=bs4.BeautifulSoup(r.content,"html.parser")
#items=soup.find_all('div',class_="caption")

print(soup)
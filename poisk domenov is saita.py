import requests
import bs4
import re
sait=dict()
finish=list()
domen=[]
url='http://pastebin.com/raw/hfMThaGb'
page = requests.get(url)
url_pattern = re.compile(r'<a.*?href=[\"|\'](.*?:\/\/)?(\w.*?)([/|:].*)?["|\'].*')
links = sorted(set([link[1] for link in url_pattern.findall(page.text)]))
print(*links, sep='\n')
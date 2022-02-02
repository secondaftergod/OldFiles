import requests
import json
def blin(inx):
    url='http://numbersapi.com/{}/math?json=true'.format(str(inx))
    headers={"User-Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1'}
    r=requests.get(url,headers=headers)
    fin=json.loads(r.text)
    if fin['found']==True:
        print('Interesting')
    else:
        print('Boring')
with open('in.txt') as file_in:
    for line in file_in:
        line=line.strip()
        x=line
        blin(x)

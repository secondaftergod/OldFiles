import requests
import reZADACHI

url='https://stepic.org/media/attachments/course67/3.6.3/699991.txt'

def req(sulka):
    r=requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+sulka)
    return r.text

krok=reZADACHI.findall(r'/(\w+.\w+)', url)
sulka=krok[-1]

def chek(we):
    a=reZADACHI.findall(r'^\w+', str(we))
    if a[0]=='We':
        return False
v=req(sulka)
while True:
    krok_2=v
    print(v)
    if chek(krok_2)==False:
        with open("out.txt", 'w') as file_out:
            file_out.write(krok_2)
        break
    v=req(krok_2)

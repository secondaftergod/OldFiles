import requests
import json


fin=dict()
client_id = '56ff4051e90b99d24e44'
client_secret = '27c19e94fb1dd72d4f6f1f774c670edf'
# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
# разбираем ответ сервера
j = json.loads(r.text)
# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
artists = []

with open('in.txt') as file:
    for artist_id in file:
        artist_id = artist_id.strip()
        url = 'https://api.artsy.net/api/artists/{}'.format(artist_id)
        params = {'xapp_token': token}
        resp = requests.get(url, params=params).text
        data = json.loads(resp)
        artists.append({'name': data['sortable_name'], 'birthday': data['birthday']})

for artist in sorted(artists, key=lambda x: (x['birthday'], x['name'])):
    print(artist['name'])



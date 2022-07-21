import requests

url='http://ddragon.leagueoflegends.com/cdn/12.13.1/data/ko_KR/Aatrox.json'
url3='http://ddragon.leagueoflegends.com/cdn/12.13.1/data/ko_KR/Amumu.json'
res=requests.get(url).json()

champ_lst=(res['data']['Aatrox']['key'], res['data']['Aatrox']['name'])
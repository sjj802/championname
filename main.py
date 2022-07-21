import requests

url='http://ddragon.leagueoflegends.com/cdn/12.13.1/data/ko_KR/Aatrox.json'
url2='http://ddragon.leagueoflegends.com/cdn/12.13.1/data/ko_KR/Ahri.json'
url3='http://ddragon.leagueoflegends.com/cdn/12.13.1/data/ko_KR/Amumu.json'

res=requests.get(url).json()
res2=requests.get(url3).json()
res3 = requests.get(url2).json()

champ_lst=(res['data']['Aatrox']['key'], res['data']['Aatrox']['name'])
champ_lst2=(res2['data']['Amumu']['key'], res2['data']['Amumu']['name'])
champ_lst3=(res3['data']['Ahri']['key'], res2['data']['Ahri']['name'])

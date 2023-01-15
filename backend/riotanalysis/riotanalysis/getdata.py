import requests
import json
import pandas as pd
import time

api_key = 'RGAPI-44d599e3-3f19-4ae9-8394-4b2754e7432a'

# get master user informations
url = "https://kr.api.riotgames.com/tft/league/v1/master?api_key=" + api_key
r = requests.get(url)

tier = r.json()['tier']
leagueId = r.json()['leagueId']
queue = r.json()['queue']
data = r.json()['entries']
df = pd.DataFrame.from_dict(data)
summonerIds = df['summonerId']

puuids = []
for summonerId in summonerIds:
  get_puuid_url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/"+ summonerId + "?api_key=" + api_key
  try:
    r = requests.get(get_puuid_url)
    
    while r.status_code == 429:
            time.sleep(5)
            r = requests.get(get_puuid_url)
  except:
        pass
  puuid = r.json()['puuid']
  puuids.append(puuid)

s_puuids = pd.Series(puuids, index =range(len(puuids)))
df = pd.concat([df, s_puuids], axis = 1)
df.rename(columns = {0: 'puuid'}, inplace = True)
df = df[['summonerId', 'summonerName', 'puuid','leaguePoints', 'rank', 'wins', 'losses',
       'veteran', 'inactive', 'freshBlood', 'hotStreak']]
df.to_csv("TFTMaterUserInfo.csv", index = False)
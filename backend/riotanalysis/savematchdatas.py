import os
import json
import pandas as pd
import requests
from pathlib import Path
import time

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")

import django
django.setup()

from riotanalysisapp.models import MatchData

#----------------------------------------------------------------------------------------------
#API Keys
BASE_DIR = Path(__file__).resolve().parent

# SECURITY WARNING: keep the secret key used in production secret!
secret_file = os.path.join(BASE_DIR, 'secrets.json')  # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        print(error_msg)
SECRET_KEY = get_secret("SECRET_KEY")

api_key = get_secret("RIOT_API_KEY")
#----------------------------------------------------------------------------------------------

data = pd.read_csv('TFTMasterUserInfo.csv')
puuids = data[['puuid']].values.tolist()

puuid = puuids[0][0] # 반복문 적용 시 [i][i]로 변경

get_match_id_url = "https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/" + puuid + "/ids?start=0&count=20&api_key=" + api_key
r = requests.get(get_match_id_url)
recentMatchIds = r.json()

# for matchid in recentMatchIds:
#     get_match_datas_url = "https://asia.api.riotgames.com/tft/match/v1/matches/" + matchid + "?api_key=" + api_key
#     try:
#         r = requests.get(get_match_datas_url)
  
#         while r.status_code == 429:
#             time.sleep(5)
#             r = requests.get(get_match_datas_url)
#     except:
#       pass
    
#     result = r.json()
#     position = result['metadata']['participants'].index(puuid)
#     info = result['info']['participants'][position]

# augments = info['augments']
# companion = info['companion']
# last_round = info['last_round']
# level = info['level']
# placement = info['placement']
# time_eliminated = info['time_eliminated']
# traits = info['traits']

# print(info)

match_id = recentMatchIds[2]
get_match_datas_url = "https://asia.api.riotgames.com/tft/match/v1/matches/" + match_id + "?api_key=" + api_key
try:
  r = requests.get(get_match_datas_url)
  
  while r.status_code == 429:
    time.sleep(5)
    r = requests.get(get_match_datas_url)
except:
      pass
result = r.json()

position = result['metadata']['participants'].index(puuid)
info = result['info']['participants'][position]

units = info['units']
champions_list = []
tiers_list = []
items_list = []

for i in range(len(units)):
    unit_info = units[i] 
    character_id = unit_info['character_id']
    tier = str(unit_info['tier'])
    
    item_list = unit_info['items']
    # item_list는 list 형식이므로 하나의 string으로 변환
    item_str = ""
    for item in item_list:
        item_str += ("-" + str(item))

    # list에 append
    champions_list.append(character_id)
    tiers_list.append(tier)
    items_list.append(item_str)

# traits 처리
traits = info['traits']
traits_list = []
for i in range(len(traits)):
    trait_info = traits[i]
    traits_list.append(trait_info['name'] + "-" + str(trait_info['style']))

# MatchData.objects.create(
#     puuid = info['puuid'],
#     last_level = info['level'],
#     placement = info['placement'],
#     last_round = info['last_round'],
#     play_time = info['time_eliminated'],
#     gold_left = info['gold_left'],
#     total_damage_to_players = info['total_damage_to_players'],

#     augments = info['augments'],
#     traits = traits_list,
#     champions = champions_list,
#     tiers = tiers_list,
#     items = items_list,
# )
print(traits_list)




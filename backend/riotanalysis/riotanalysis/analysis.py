import os
import json
import pandas as pd
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

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

data = pd.read_csv('TFTMasterUserInfo.csv')
puuids = data[['puuid']].values.tolist()

puuid = puuids[0][0] # 반복문 적용 시 [i][i]로 변경

get_match_id_url = "https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/" + puuid + "/ids?start=0&count=20&api_key=" + api_key
r = requests.get(get_match_id_url)
recentMatchIds = r.json()

for matchid in recentMatchIds:
    get_match_datas_url = "https://asia.api.riotgames.com/tft/match/v1/matches/" + matchid + "?api_key=" + api_key
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

augments = info['augments']
companion = info['companion']
last_round = info['last_round']
level = info['level']
placement = info['placement']
time_eliminated = info['time_eliminated']
traits = info['traits']

print(info)

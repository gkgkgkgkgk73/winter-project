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
data = pd.read_csv('TFTMasterUserInfo.csv') # 처음 시작할 당시 마스터 티어 유저들 데이터
puuids = data[['puuid']].values.tolist()


for j in range(len(puuids)):
    
    # for test
    # if j > 0:
    #     break

    puuid = puuids[j][0] # j번째는 리스트이므로 0번째 참조해서 str으로

    get_match_id_url = "https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/" + puuid + "/ids?start=0&count=20&api_key=" + api_key
    r = requests.get(get_match_id_url)
    recentMatchIds = r.json()

    for i in range(len(recentMatchIds)):
        
        # for test
        # if i > 0:
        #     break

        match_id = recentMatchIds[i]
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
        units_json = json.dumps(units)

        traits = info['traits']
        traits_json = json.dumps(traits)

        augments = info['augments']
        augments_json = json.dumps(augments)

        game_type = result['info']['tft_game_type']
        set_num = result['info']['tft_set_number']

        exist = MatchData.objects.filter(
            puuid = puuid,
            match_id = match_id 
        ).values().count()
        # exist == 0 이면 새로 받은 데이터가 DB에 없는 것.

        if exist == 0:        
            MatchData.objects.create(
                match_id = match_id,
                puuid = info['puuid'],
                game_type = game_type,
                set_number = set_num,
                last_level = info['level'],
                placement = info['placement'],
                last_round = info['last_round'],
                play_time = info['time_eliminated'],
                gold_left = info['gold_left'],
                total_damage_to_players = info['total_damage_to_players'],

                augments = augments_json,
                traits = traits_json,
                units = units_json
            )
        


    # 이건 test용    
    if j % 10 == 0:
        print('Order: ' + str(j) + 'th of ' + str(len(puuids)))
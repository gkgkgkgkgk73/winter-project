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
from riotanalysisapp.models import MatchData, Augment
from django.db.models import Q

# augments 전체 데이터
augments_str = ['augments1','augments2','augments3']

for j in range(len(augments_str)):
    df = MatchData.objects.values(augments_str[j])
    length = len(df)
    augments_list = []

    for i in range(length):
        data = df[i]['augments'+ str(j+1)]
        augments_list.append(data)

augments_list = list(set(augments_list))
#print((augments_list)) #: current 272
zero_inplated_augments_list = augments_list[1:]


data = []
for i in range(len(zero_inplated_augments_list)):
    target = zero_inplated_augments_list[i]
    
    queryset = MatchData.objects.all().values('id', 'placement', 'augments1')
    total_games_num = len(queryset)
    result = queryset.filter( (Q(augments1 = target)) & Q(game_type = 'standard'))
    pick_count = len(result)
    
    pick_rate = 0
    if total_games_num > 0:
        pick_rate = pick_count / total_games_num

    win_count = 0
    for item in result:
        if item['placement'] < 5:
            win_count = win_count + 1

    win_rate = 0
    if len(result) > 0:
        win_rate = win_count / len(result)

    dat = [win_rate, pick_rate, win_count, len(result), target]
    data.append(dat)
    #print("Win rate is " + str(win_rate) + "/ " + str(win_count) + "/ " + str(len(result)))    

    #if i > 9: break

df = pd.DataFrame(data, columns = ['win rate', 'pick rate', 'win count', 'total games', 'first_augment_name'])
df_upper30 = df.loc[df['total games'] > 29] # 30판 이상 기록만 걸러냄
#print(df_upper10.sort_values('total games', ascending=False))
#df.to_csv("C:/Users/gangg/win_rate.csv")

df_upper30_sorted_by_total_games = df_upper30.sort_values('total games', ascending=False)

kor_name_list = []
for name in df_upper30_sorted_by_total_games['first_augment_name'].to_list():
    kor_name = Augment.objects.get(augment_apiName = name).augment_name
    kor_name_list.append(kor_name)

df_upper30_sorted_by_total_games['kor_augment_name'] = kor_name_list
df_upper30_sorted_by_total_games.to_csv("C:/Users/gangg/winter-project/backend/riotanalysis/riotanalysisapp/first_augment_result.csv", index = False)






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
from django.db.models import Q

"""
df = MatchData.objects.values('last_level')
last_levels = []
for level in df:
    last_levels.append(level['last_level'])

df = MatchData.objects.values('placement')
top4 = []
for place in df:
    rank = place['placement']
    istop4 = 0
    if rank > 4:
        istop4 = False
    else:
        istop4 = True
    top4.append(istop4)
"""
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
    
    queryset = MatchData.objects.all().values('id', 'placement', 'augments1', 'augments2', 'augments3')
    result = queryset.filter( (Q(augments1 = target) | Q(augments2 = target) | Q(augments3 = target)) & Q(game_type = 'standard'))
    
    win_count = 0
    for item in result:
        if item['placement'] < 5:
            win_count = win_count + 1

    win_rate = 0
    if len(result) > 0:
        win_rate = win_count / len(result)

    dat = [win_rate, win_count, len(result), target]
    data.append(dat)
    #print("Win rate is " + str(win_rate) + "/ " + str(win_count) + "/ " + str(len(result)))    

    #if i > 9: break

df = pd.DataFrame(data, columns = ['win rate', 'win count', 'total games', 'augment_name'])
df_upper10 = df.loc[df['total games'] > 9]
print(df_upper10.sort_values('win rate', ascending=False))

#df.to_csv("C:/Users/gangg/win_rate.csv")
 






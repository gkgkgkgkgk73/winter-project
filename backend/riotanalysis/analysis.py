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
df = MatchData.objects.values('augments')
length = len(df)
augments_list = []

for i in range(length):
    data = df[i]['augments']
    data = data.split('"')
    data = [item for item in data if len(item) > 2]

    for item in data:
        augments_list.append(item)

augments_list = list(set(augments_list))
# print(len(augments_list)) : current 272

target = augments_list[0]

queryset = MatchData.objects.all().values('id', 'placement', 'augment1', 'augment2', 'augment3')
print(queryset)


#result = queryset.filter(Q(augment1 = target) | Q(augment2 = target) | Q(augment3 = target))
#print(result)





#filter할 때 더블업 제외




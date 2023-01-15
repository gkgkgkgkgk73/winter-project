import os
import json
import pandas as pd
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")
import django
django.setup()
from riotanalysisapp.models import MatchData, BaseItem, UpperItem
from django.db.models import Q

queryset = MatchData.objects.all().values('units')
#query = queryset[0]
# a = json.loads(query['units'])
# print(a[3])

unit_item_dict = dict()
for query in queryset:
    js = json.loads(query['units'])
    
    for inform in js:
        name = inform['character_id']
        item_list = inform['items']
        
        if name in unit_item_dict:
            old = unit_item_dict[name]
            for item in item_list:
                old.append(item)
            unit_item_dict[name] = old
        else:
            unit_item_dict[name] = item_list

# champion_name_list는 시즌8 모든 챔피언 리스트(순서, 특성X), 59개
champion_name_list = ['TFT8_Janna', 'TFT8_Samira', 'TFT8_Kaisa', 'TFT8_Jax', 'TFT8_Velkoz', 'TFT8_WuKong', 'TFT8_Lux', 'TFT8_Ekko', 'TFT8_Blitzcrank', 'TFT8_Yasuo', 'TFT8_Yuumi', 'TFT8_Gangplank', 'TFT8_Soraka', 'TFT8_Zed', 
'TFT8_Sejuani', 'TFT8_Malphite', 'TFT8_Taliyah', 'TFT8_Galio', 'TFT8_Jinx', 'TFT8_BelVeth', 'TFT8_Viego', 'TFT8_Rammus', 'TFT8_Vi', 'TFT8_Nunu', 'TFT8_Aphelios', 'TFT8_Zac', 'TFT8_Renekton', 'TFT8_Annie', 'TFT8_Leona', 'TFT8_Sivir', 'TFT8_Ashe', 'TFT8_Sett', 'TFT8_Rell', 'TFT8_Senna', 'TFT8_Lulu', 'TFT8_Camille', 'TFT8_Urgot', 'TFT8_Leblanc', 'TFT8_Nilah', 'TFT8_Riven', 'TFT8_Mordekaiser', 'TFT8_Fiora', 'TFT8_Kayle', 'TFT8_Ezreal', 'TFT8_Syndra', 'TFT8_Vayne', 'TFT8_Sylas', 'TFT8_Nasus', 'TFT8_Fiddlesticks', 'TFT8_Poppy', 'TFT8_LeeSin', 'TFT8_Alistar', 'TFT8_AurelionSol', 'TFT8_Chogath', 'TFT8_MissFortune', 'TFT8_Sona', 'TFT8_Talon', 'TFT8_Draven', 'TFT8_Zoe']

base = BaseItem.objects.all().values('item_id', 'item_name')
upper = UpperItem.objects.all().values('item_id', 'item_name')
id_name_dict = dict()
for element in base:
    id = element['item_id']
    name = element['item_name']
    id_name_dict[id] = name
for element in upper:
    id = element['item_id']
    name = element['item_name']
    id_name_dict[id] = name

most_item_champion_dict = dict()
for name in champion_name_list:
    item_dict = dict()
    for item in unit_item_dict[name]:
        if item in item_dict:
            item_dict[item] += 1
        else:
            item_dict[item] = 1

    most_item_name_list = []
    sorted_list = sorted(item_dict.items(), key=lambda x: x[1], reverse = True)[0:6]
    for tuple in sorted_list:
        item_id = tuple[0]
        most_item_name_list.append(id_name_dict[item_id])
    most_item_champion_dict[name] = most_item_name_list

# for champion in champion_name_list:
#     a = ", ".join(most_item_champion_dict[champion])
#     print(champion + " " + a + "\n")
print(id_name_dict)
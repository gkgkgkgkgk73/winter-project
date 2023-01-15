import pandas as pd
import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")
import django
django.setup()
from riotanalysisapp.models import ItemStat
from django.db.models import Q

df = pd.read_csv('champion_item_data.csv')

champion_name_list = ['TFT8_Janna', 'TFT8_Samira', 'TFT8_Kaisa', 'TFT8_Jax', 'TFT8_Velkoz', 'TFT8_WuKong', 'TFT8_Lux', 'TFT8_Ekko', 'TFT8_Blitzcrank', 'TFT8_Yasuo', 'TFT8_Yuumi', 'TFT8_Gangplank', 'TFT8_Soraka', 'TFT8_Zed', 
'TFT8_Sejuani', 'TFT8_Malphite', 'TFT8_Taliyah', 'TFT8_Galio', 'TFT8_Jinx', 'TFT8_BelVeth', 'TFT8_Viego', 'TFT8_Rammus', 'TFT8_Vi', 'TFT8_Nunu', 'TFT8_Aphelios', 'TFT8_Zac', 'TFT8_Renekton', 'TFT8_Annie', 'TFT8_Leona', 'TFT8_Sivir', 'TFT8_Ashe', 'TFT8_Sett', 'TFT8_Rell', 'TFT8_Senna', 'TFT8_Lulu', 'TFT8_Camille', 'TFT8_Urgot', 'TFT8_Leblanc', 'TFT8_Nilah', 'TFT8_Riven', 'TFT8_Mordekaiser', 'TFT8_Fiora', 'TFT8_Kayle', 'TFT8_Ezreal', 'TFT8_Syndra', 'TFT8_Vayne', 'TFT8_Sylas', 'TFT8_Nasus', 'TFT8_Fiddlesticks', 'TFT8_Poppy', 'TFT8_LeeSin', 'TFT8_Alistar', 'TFT8_AurelionSol', 'TFT8_Chogath', 'TFT8_MissFortune', 'TFT8_Sona', 'TFT8_Talon', 'TFT8_Draven', 'TFT8_Zoe']

pick_count = []
win_count = []
# for name in champion_name_list:
#     subdf = df[ df['champion_name'] == name ]

for name in champion_name_list:
    subdf = df[ df['champion_name'] == name ][['item_name', 'is_top4']]
    item_list = list(set(subdf['item_name'].values.tolist()))
    for item in item_list:
        new_df = subdf[subdf['item_name'] == item]
        pick = len(new_df)
        win = len(new_df[new_df['is_top4'] == True])
        win_rate = win/pick
        pick_rate = len(new_df)/len(subdf)
        if pick > 29:
            ItemStat.objects.create(
                champion_name = name,
                item_name = item,
                pick_count = pick,
                win_count = win,
                pick_rate = pick_rate,
                win_rate = win_rate
            )
        

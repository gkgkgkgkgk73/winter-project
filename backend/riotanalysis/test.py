import os
import json
import pandas as pd
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")
import django
django.setup()
from riotanalysisapp.models import MatchData
from django.db.models import Q
import matplotlib.pyplot as plt

queryset = MatchData.objects.all().values()

def get_most_2_traits(query):
    traits_list = query['traits']
    traits_list = json.loads(traits_list)
    
    trait_name_list = []
    for trait in traits_list:
        if trait['tier_current'] > 1:
            trait_name = trait['name']
            trait_name_list.append(trait_name.split('_')[1])
    
    return ' '.join(sorted(trait_name_list))

def get_3_items_champions(query):
    units_list = query['units']
    units_list = json.loads(units_list)
    
    unit_name_list = []
    for unit in units_list:
        if len(unit['items'])> 2:
            name = unit['character_id']
            unit_name_list.append(name.split('_')[1])

    return ' '.join(sorted(unit_name_list))
     
result = {}
placement_result = {}
for query in queryset:
    placement = query['placement']

    trait_name = get_most_2_traits(query)
    champions_name = get_3_items_champions(query)
    if len(trait_name) > 0 and len(champions_name) > 0:
        total_deck_name =  trait_name + ' ' + champions_name
        
        if total_deck_name in result:
            result[total_deck_name] += 1
            placement_result[total_deck_name] += placement
        else:
            result[total_deck_name] = 1
            placement_result[total_deck_name] = placement

key_list = list(result.keys())
for key in key_list:
    if result[key] > 50:
        print(str(key) + ': ' + str(result[key]) + ', average: ' + str(round(placement_result[key]/result[key],2)))

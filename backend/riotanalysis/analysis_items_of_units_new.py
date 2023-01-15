import os
import json
import pandas as pd
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")
import django
django.setup()
from riotanalysisapp.models import MatchData, BaseItem, UpperItem, Champion
from django.db.models import Q

# item의 id-name dictionary
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

# dataframe을 위한 이중 리스트
queryset = MatchData.objects.all().values()
result = []

for query in queryset:
    placement = query['placement']
    is_top4 = True if placement < 5 else False
    units = query['units']
    units_json = json.loads(units)
    for unit in units_json:
        name = unit['character_id']
        item_list = unit['items']

        sub_query1 = Champion.objects.all().filter(champion_apiName = name).values('champion_cost')
        cost = sub_query1[0]['champion_cost']
        if len(item_list) == 0:
            pass
        else:
            for item_id in item_list:
                item_name = id_name_dict[item_id]
                sub_result = [cost, name, item_name, placement, is_top4]
                result.append(sub_result)

df = pd.DataFrame(result, columns = ['cost', 'champion_name', 'item_name', 'placement', 'is_top4']) 
df.to_csv('champion_item_data.csv', index = False)

    



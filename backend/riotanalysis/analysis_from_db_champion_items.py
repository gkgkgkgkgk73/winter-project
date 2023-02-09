import pandas as pd
import json
import os
from tabulate import tabulate

os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")
import django
django.setup()
from riotanalysisapp.models import ItemStat
from django.db.models import Q

input_name = input("챔피언의 이름을 입력하세요 : ")
order_type = input("정렬 기준을 선택하세요. 픽률: 1, 승률: 2: ")

query_set = ItemStat.objects.all().filter(Q(champion_name = input_name)).values()
data = []
for query in query_set:
    item_name = query['item_name']
    pick_rate = query['pick_rate']
    pick_rate = round(pick_rate, 3) * 100
    win_rate = query['win_rate']
    win_rate = round(win_rate, 3) * 100
    data.append([item_name, pick_rate, win_rate])
df = pd.DataFrame(data, columns=['item_name', 'pick_rate', 'win_rate'])
# print(tabulate(df.sort_values(by = df.columns[int(order_type)], ascending=False), headers = 'keys', tablefmt= 'psql', showindex=True, stralign='center', numalign='center' ))
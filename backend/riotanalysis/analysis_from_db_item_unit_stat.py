import os
import json
import pandas as pd
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")
import django
django.setup()
from riotanalysisapp.models import ItemStat, MatchData
from django.db.models import Q
import matplotlib.pyplot as plt

# 설명
# 챔피언 픽률은 전체 매치데이터 중 해당 챔피언을 포함한 기록의 비율(아이템의 유무는 고려 X)
# 아이템 픽률은 아이템을 넣은 경우 중 해당 아이템을 가진 비율(아이템을 안넣은 경우는 고려 X)

champion_name_list = ['TFT8_Janna', 'TFT8_Samira', 'TFT8_Kaisa', 'TFT8_Jax', 'TFT8_Velkoz', 'TFT8_WuKong', 'TFT8_Lux', 'TFT8_Ekko', 'TFT8_Blitzcrank', 'TFT8_Yasuo', 'TFT8_Yuumi', 'TFT8_Gangplank', 'TFT8_Soraka', 'TFT8_Zed', 
'TFT8_Sejuani', 'TFT8_Malphite', 'TFT8_Taliyah', 'TFT8_Galio', 'TFT8_Jinx', 'TFT8_BelVeth', 'TFT8_Viego', 'TFT8_Rammus', 'TFT8_Vi', 'TFT8_Nunu', 'TFT8_Aphelios', 'TFT8_Zac', 'TFT8_Renekton', 'TFT8_Annie', 'TFT8_Leona', 'TFT8_Sivir', 'TFT8_Ashe', 'TFT8_Sett', 'TFT8_Rell', 'TFT8_Senna', 'TFT8_Lulu', 'TFT8_Camille', 'TFT8_Urgot', 'TFT8_Leblanc', 'TFT8_Nilah', 'TFT8_Riven', 'TFT8_Mordekaiser', 'TFT8_Fiora', 'TFT8_Kayle', 'TFT8_Ezreal', 'TFT8_Syndra', 'TFT8_Vayne', 'TFT8_Sylas', 'TFT8_Nasus', 'TFT8_Fiddlesticks', 'TFT8_Poppy', 'TFT8_LeeSin', 'TFT8_Alistar', 'TFT8_AurelionSol', 'TFT8_Chogath', 'TFT8_MissFortune', 'TFT8_Sona', 'TFT8_Talon', 'TFT8_Draven', 'TFT8_Zoe']

def get_item_tier(input_name):
    # input_name = input("챔피언 이름을 입력하세요: ")
    # input_sort_type = input("정렬 방법을 선택하세요.\n픽률: 1, 승률: 2, 동시: 3 ")

    name = input_name
    queryset = ItemStat.objects.filter(champion_name = name).values()
    result = []
    for query in queryset:
        pick_rate = round(query['pick_rate'] * 100, 2)
        win_rate = round(query['win_rate'] * 100, 2)
        value = pick_rate ** 2 + (win_rate/10) ** 2
        sub = [query['item_name'], pick_rate , win_rate, value]
        result.append(sub)
    df = pd.DataFrame(result, columns=['item_name', 'pick_rate', 'win_rate', 'value'])
    #df = df.sort_values('value', ascending=False)
    # if input_sort_type == 1:
    #     type = 'pick_rate'
    # elif input_sort_type == 2:
    #     type = 'win_rate'
    # else:
    #     type = 'value'

    # df = df.sort_values(type, ascending=False)
    return df    

# return은 길이 2 list, 첫번째 값은 champion_win_rate, 두번째 값은 champion_pick_rate
def get_champion_stat(champion_name):
    queryset = MatchData.objects.all().values()
    game_size = len(queryset)

    win_count = 0
    pick_count = 0

    for query in queryset:
        placement = query['placement']
            
        units = json.loads(query['units'])
        for unit in units:
            if unit['character_id'] != champion_name:
                pass
            else:
                pick_count += 1
                if placement < 5:
                    win_count += 1
    win_rate = 0
    if pick_count > 0:
        win_rate = win_count / pick_count
    return [round(win_rate * 100, 2), round(pick_count/game_size * 100, 2)]

for name in champion_name_list:
    df = get_item_tier(name)
    pick_rate = list(df['pick_rate'])
    win_rate = list(df['win_rate'])

    # 챔피언 평균 승률
    champion_win_rate = get_champion_stat(name)[0]
    # 챔피언 평균 픽률
    # 픽률은 뭔가 이상해서 잠시 뺏음.
    #champion_pick_rate = get_champion_stat(name)[1]

    plt.scatter(pick_rate, win_rate, s= 5, c = 'k')

    # 점에 라벨 붙이기
    for i in range(len(df)):
        row = df.iloc[i] # 한 행씩 꺼내기
        item_name = row['item_name'] 
        x = row['pick_rate'] # x좌표가 저장된 열
        y = row['win_rate'] # y좌표가 저장된 열
        plt.text(x, y, item_name, fontsize = 'small')
    
    plt.axhline(y=champion_win_rate, color='r', linewidth=1, linestyle='--')
    #plt.axvline(x=champion_pick_rate, color='r', linewidth=1, linestyle='--')

    plt.xlabel('pick_rate')
    plt.ylabel('win_rate')
    plt.title(name)

    path = 'itemgraphs/' + name + '.png'
    plt.savefig(path)
    plt.clf()
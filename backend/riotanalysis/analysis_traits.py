import os
import json
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")
import django
django.setup()
from riotanalysisapp.models import MatchData, Champion
from django.db.models import Q

from sklearn.cluster import KMeans

# 챔피언 보유 현황을 바탕으로(몇성인지, 어떤 아이템을 가지고 있는지는 고려 X) k-means clustering 진행

# 모든 유닛 리스트

# queryset = Champion.objects.all().values('champion_apiName')

# champion_name_list = []
# for query in queryset:
#     name = query['champion_apiName']
#     season = name.split('_')[0]
#     if season == 'TFT8':
#         champion_name_list.append(name)
# champion_name_list = list(set(champion_name_list))
# champion_name_list는 시즌8 모든 챔피언 리스트(순서, 특성X), 59개
champion_name_list = ['TFT8_Janna', 'TFT8_Samira', 'TFT8_Kaisa', 'TFT8_Jax', 'TFT8_Velkoz', 'TFT8_WuKong', 'TFT8_Lux', 'TFT8_Ekko', 'TFT8_Blitzcrank', 'TFT8_Yasuo', 'TFT8_Yuumi', 'TFT8_Gangplank', 'TFT8_Soraka', 'TFT8_Zed', 
'TFT8_Sejuani', 'TFT8_Malphite', 'TFT8_Taliyah', 'TFT8_Galio', 'TFT8_Jinx', 'TFT8_BelVeth', 'TFT8_Viego', 'TFT8_Rammus', 'TFT8_Vi', 'TFT8_Nunu', 'TFT8_Aphelios', 'TFT8_Zac', 'TFT8_Renekton', 'TFT8_Annie', 'TFT8_Leona', 'TFT8_Sivir', 'TFT8_Ashe', 'TFT8_Sett', 'TFT8_Rell', 'TFT8_Senna', 'TFT8_Lulu', 'TFT8_Camille', 'TFT8_Urgot', 'TFT8_Leblanc', 'TFT8_Nilah', 'TFT8_Riven', 'TFT8_Mordekaiser', 'TFT8_Fiora', 'TFT8_Kayle', 'TFT8_Ezreal', 'TFT8_Syndra', 'TFT8_Vayne', 'TFT8_Sylas', 'TFT8_Nasus', 'TFT8_Fiddlesticks', 'TFT8_Poppy', 'TFT8_LeeSin', 'TFT8_Alistar', 'TFT8_AurelionSol', 'TFT8_Chogath', 'TFT8_MissFortune', 'TFT8_Sona', 'TFT8_Talon', 'TFT8_Draven', 'TFT8_Zoe']

queryset = MatchData.objects.all().values('units')

total_result = []
for query in queryset:
    data = query['units']
    units = json.loads(data)

    units_index = []
    for unit in units:
        name = unit['character_id']
        units_index.append(champion_name_list.index(name))

    result = [0 for i in range(59)]
    for index in units_index:
        result[index] = 1
    total_result.append(result)

df = pd.DataFrame(total_result, columns = champion_name_list)
points = df.values

# elbow method 시각화: 특정한 구간이 보이진 않지만 12개?
# --------------------------------------------------
# distortions = []
# K = range(1, 20)
# for k in K:
#     kmeans = KMeans(n_clusters = k).fit(points)
#     distortions.append(kmeans.inertia_)

# plt.figure(figsize=(16,8))
# plt.plot(K, distortions, 'bx-')
# plt.xlabel('k')
# plt.ylabel('Distortion')
# plt.title('The Elbow Method showing the optimal k')
# plt.show()

kmeans = KMeans(n_clusters = 12).fit(points)
centers = kmeans.cluster_centers_
new_centers = []
for center in centers:
    subresult = []
    for number in center:
        if number < 0.2: num = 0
        elif number > 0.8: num = 1
        else: num = number
        num = number
        subresult.append(num)
    new_centers.append(subresult)
    # num digit 줄이기

# for j in range(12):
#     main_champions = []
#     for i in range(59):
#         if new_centers[j][i] > 0.4:
#             main_champions.append(champion_name_list[i])

#     for champion in main_champions:
#         Champion.objects.all('values')

#     print("#" + str(j+1) + "th " + "main champions are: " + ' '.join(main_champions))    
    
#     print('------------------------\n')

#      # + 시너지 합 계산

a = Champion.objects.all().values('id','champion_apiName')
b = a.filter(Q(champion_apiName = 'TFT8_Leblanc'))
print(b)




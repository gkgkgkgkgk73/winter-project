import os
import json
import pandas as pd
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")
import django
django.setup()
from riotanalysisapp.models import Champion, Trait
from django.db.models import Q

def make_prob_json():
    level_champion_prob = [[0.75, 0.25, 0, 0, 0], [0.55, 0.3, 0.15, 0, 0], [0.45, 0.33, 0.2, 0.02, 0], [0.25, 0.4, 0.3, 0.05, 0], [0.19, 0.3, 0.35, 0.15, 0.01], [0.16, 0.2, 0.35, 0.25, 0.04], [0.09, 0.15, 0.3, 0.3, 0.16], [0.05, 0.1, 0.2, 0.4, 0.25]]
    # 3~10 level
    champion_name_list = ['TFT8_Janna', 'TFT8_Samira', 'TFT8_Kaisa', 'TFT8_Jax', 'TFT8_Velkoz', 'TFT8_WuKong', 'TFT8_Lux', 'TFT8_Ekko', 'TFT8_Blitzcrank', 'TFT8_Yasuo', 'TFT8_Yuumi', 'TFT8_Gangplank', 'TFT8_Soraka', 'TFT8_Zed', 
    'TFT8_Sejuani', 'TFT8_Malphite', 'TFT8_Taliyah', 'TFT8_Galio', 'TFT8_Jinx', 'TFT8_BelVeth', 'TFT8_Viego', 'TFT8_Rammus', 'TFT8_Vi', 'TFT8_Nunu', 'TFT8_Aphelios', 'TFT8_Zac', 'TFT8_Renekton', 'TFT8_Annie', 'TFT8_Leona', 'TFT8_Sivir', 'TFT8_Ashe', 'TFT8_Sett', 'TFT8_Rell', 'TFT8_Senna', 'TFT8_Lulu', 'TFT8_Camille', 'TFT8_Urgot', 'TFT8_Leblanc', 'TFT8_Nilah', 'TFT8_Riven', 'TFT8_Mordekaiser', 'TFT8_Fiora', 'TFT8_Kayle', 'TFT8_Ezreal', 'TFT8_Syndra', 'TFT8_Vayne', 'TFT8_Sylas', 'TFT8_Nasus', 'TFT8_Fiddlesticks', 'TFT8_Poppy', 'TFT8_LeeSin', 'TFT8_Alistar', 'TFT8_AurelionSol', 'TFT8_Chogath', 'TFT8_MissFortune', 'TFT8_Sona', 'TFT8_Talon', 'TFT8_Draven', 'TFT8_Zoe']

    champ_level_prob_result_dict = {}
    for name in champion_name_list:
        traits_queryset = Champion.objects.all().filter(champion_apiName = name).values('traits')
        num_units_each_tiers = [0, 0, 0, 0, 0]

        used_id = []
        name_cost_dict = {}
        for query in traits_queryset:
            trait_id = query['traits']
            champion_queryset = Champion.objects.all().filter(traits = trait_id).values('id')
            for query in champion_queryset:
                id = query['id']
                if id in used_id:
                    pass
                else:
                    cost = Champion.objects.filter(id = id).values('champion_cost')[0]['champion_cost']       
                    apiname = Champion.objects.filter(id = id).values('champion_apiName')[0]['champion_apiName']
                    name_cost_dict[apiname] = cost
                    num_units_each_tiers[int(cost)-1] += 1
                    used_id.append(id)

        sorted_by_cost = sorted(name_cost_dict.items(), key = lambda item: item[1], reverse = False)
        sorted_by_cost_list = []
        for item in sorted_by_cost:
            sorted_by_cost_list.append(item[0])
        # print(sorted_by_cost_list)

        result_dict = {}
        for level in range(3, 11):
            result = []
            probs = level_champion_prob[level - 3]
            for tier in range(1, 6):
                num_units_tier = num_units_each_tiers[tier - 1]
                if num_units_tier > 0:
                    prob = 100 * probs[tier - 1] / num_units_tier
                else:
                    prob = 0
                
                for i in range(num_units_tier):
                    result.append(prob)
            sum_prob = sum(result)
            
            if sum_prob > 0:
                for i in range(len(result)):
                    result[i] = round(result[i] * 100 / sum_prob,2)
                
       
            null_dict = {}
            for i in range(len(result)):
                null_dict[sorted_by_cost_list[i]] = result[i]
            result_dict["Level " + str(level)] = null_dict
        champ_level_prob_result_dict[name] = result_dict
    return champ_level_prob_result_dict

data_json = make_prob_json()

def use_dice_on():
    input_name = input("사기주사위를 쓸 챔피언의 이름을 입력하세요 : ")
    input_level = int(input("현재 레벨을 입력하세요 : "))

    data = data_json[input_name]['Level ' + str(input_level)]
    print(data)

def want_to_roll():
    input_name = input("사기주사위를 쓸 챔피언의 이름을 입력하세요 : ")
    input_level = int(input("현재 레벨을 입력하세요 : "))
    
    champion_list = list(data_json[input_name]['Level 3'].keys())
    result_dict = {}
    for name in champion_list:
        prob = data_json[name]['Level ' + str(input_level)][input_name]
        result_dict[name] = prob
    print(result_dict)


input_type = input("챔피언에게 사용할 때 확률을 알고 싶으면 1, \n어떤 챔피언에게 사용해야 할지 알고 싶으면 2: ")

if input_type == 1:
    use_dice_on()
else:
    want_to_roll()



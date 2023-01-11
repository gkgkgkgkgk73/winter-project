import requests

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")

import django
django.setup()

from riotanalysisapp.models import BaseItem, UpperItem, Champion, Trait, Augment

url = 'https://raw.communitydragon.org/12.23/cdragon/tft/ko_kr.json'
icon_pre_url = 'https://raw.communitydragon.org/12.23/game/'
resp = requests.get(url=url)
data = resp.json()
data_items = []

def get_basic_items_info():
    for d in data['items']:
        if '_Item_' in d['apiName']:
            if not d['from']:
                BaseItem.objects.create(
                    item_id = d['id'],
                    item_name = d['name'],
                    item_img = icon_pre_url+d['icon'].lower(),
                    item_info = d['desc'],                   
                    item_apiName = d['apiName'],
                    item_effect = d['effects']
                )
    for d in data['items']:
        if '_Item_' in d['apiName']:
            if d['from']:
                new_data = UpperItem.objects.create(
                    item_id = d['id'],
                    item_name = d['name'],
                    item_img = icon_pre_url+d['icon'].lower(),
                    item_info = d['desc'],                   
                    item_apiName = d['apiName'],
                    item_effect = d['effects'],
                )
                base_1 = BaseItem.objects.filter(item_id = d['from'][0])
                base_2 = BaseItem.objects.filter(item_id = d['from'][1])
                if base_1:
                    new_data.base_items.add(base_1[0])
                if base_2:
                    new_data.base_items.add(base_2[0])
                new_data.save()
 #   for d in data_items:
        
    
    #여기 item 정보 저장하면 됨.

def get_basic_champions_info():
    for d in data['setData']:
        for c in d['champions']:
            if c['traits']:
                if Champion.objects.filter(champion_apiName = c['apiName']).count() == 0:
                    champ = Champion.objects.create(
                        champion_apiName = c['apiName'],
                        champion_variables = {'variables' : c['ability']['variables']},
                        champion_name = c['name'],
                        champion_img = icon_pre_url+c['icon'].lower(),
                        champion_info = c['ability']['desc'],
                        champion_stats = c['stats'],
                        champion_cost = c['cost']
                    )
                    for t in c['traits']:
                        temp = Trait.objects.filter(trait_name = t)
                        if temp:
                            champ.traits.add(temp[0])
                    champ.save()
    
def get_basic_traits_info():
    trait_list = data['setData']
    for d in trait_list:
        for t in d['traits']:
            if 'Set8_' in t['apiName']:
                Trait.objects.create(
                        trait_name = t['name'],
                        trait_apiName = t['apiName'],
                        trait_img = icon_pre_url+t['icon'].lower(),
                        trait_effect = {'effect': t['effects']},
                        trait_info = t['desc']
                    )

def get_basic_augments_info():
    for d in data['items']:
        if '_Augment_' in d['apiName']:
            Augment.objects.create(
                augment_id = d['id'],
                augment_name = d['name'],
                augment_img = icon_pre_url+d['icon'].lower(),
                augment_info = d['desc'],                   
                augment_apiName = d['apiName'],
                augment_effect = d['effects']
            )
            
get_basic_items_info()
get_basic_traits_info()
get_basic_champions_info()
get_basic_augments_info()
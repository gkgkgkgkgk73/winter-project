import requests

url = 'https://raw.communitydragon.org/12.23/cdragon/tft/ko_kr.json'

resp = requests.get(url=url)
data = resp.json()
data_items = []

def get_basic_items_info():
    for d in data['items']:
        if 'TFT8' in d['apiName'] or 'TFT_' in d['apiName']:
            data_items.append(d)
    print(data_items)
    #여기 item 정보 저장하면 됨.

def get_basic_champions_info():
    for d in data['setData']:
        for c in d['champions']:
            if 'TFT8' in c['apiName'] or 'TFT_' in c['apiName']:
                data_items.append(c)
    print(data_items)
    
get_basic_champions_info()
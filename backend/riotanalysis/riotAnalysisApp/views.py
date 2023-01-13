from django.shortcuts import render
from .models import Trait, UpperItem, BaseItem, Champion, Augment
from django.http import HttpResponse, JsonResponse
import json
specific_item = ['영혼의 형상','죽음의 저항','영원한 겨울', '무한한 삼위일체', '마나자네', '흑요석 양날 도끼', '란두인의 성소', '로켓 주먹', '황금 징수의 총', '존야의 역설', '우르프 천사의 지팡이', '축복받은 피바라기', '푸른 축복', '장미가시 조끼', '선의의 성배', '빛나는 죽음의 검', '용의 의지', '철갑의 서막', '수호상 돌갑옷', '악마 학살자', '새벽의 서광', '구인수의 심판', '공정의 주먹', '마법공학 생명검', '천공의 대검', '집단 충격기', '눈부신 건틀릿', '영겁의 속삭임', '타곤 정상의 펜던트', '엔젤로노미콘', '반짝이는 수은', '라바돈의 초월한 죽음모자', '고속 광자포', '면죄', '루난의 폭풍', '경외의 장막', '히라나의 창', '스태틱의 호의', '태양빛 망토', '장난꾸러기의 장갑', '거인의 맹세', '의지파괴자', '워모그의 자부심', '지크의 조화', '겨울바람', '즈롯 소환문', '메카 선택기', '에이스 상징', '방패대 상징', '톱날 피바라기', '싸움꾼 상징', '주문투척자 상징', '민간인 상징', '특등사수 상징', '엄호대 상징', '메카: 프라임 상징', '기계유망주 상징', '과부하_오류 // 거인 학살자', '해커 상징', '비결정적 정의의 손길', '자화 이온 충격기', '익살꾼 상징', '용수철이 든 고속 연사포', '정찰단 상징', '날뛰는 쇼진의 창', '더 고요한 침묵의 장막', '별 수호자 상징', '과열된 태양불꽃 망토', '지하세께 상징', '유도집전형 워모그의 갑옷', 'B.F. 대검', '곡궁', '쇠사슬 조끼', '음전자 망토', '쓸데없이 큰 지팡이', '여신의 눈물', '거인의 허리띠', '연습용 장갑', '뒤집개']

# Create your views here.
def index():
    print("Hello world!")
    
def get_trait_info(request):
    if request.method == "GET":
        result = []
        traits = Trait.objects.all()
        for trait in traits:
            data = {
                'name':trait.trait_name,
                'apiName':trait.trait_apiName,
                'img': trait.trait_img,
                'effect':trait.trait_effect['effect'],
                'info':trait.trait_info,
                'id':trait.id
            }
            result.append(data)
        return JsonResponse(list(result), status = 200, safe=False)
    else:
        return HttpResponse(status = 403)

def get_champion_info(request):
    if request.method == "GET":
        champions = Champion.objects.all()
        result = []
        for champion in champions:
            trait = []
            for t in champion.traits.all():
                trait.append(t.id)
            data = {
                'name':champion.champion_name,
                'apiName':champion.champion_apiName,
                'img': champion.champion_img,
                'variables':champion.champion_variables,
                'traits': trait,
                'info':champion.champion_info,
                'id':champion.id,
                'championStats':champion.champion_stats,
                'championCost':champion.champion_cost
            }
            result.append(data)
        return JsonResponse(list(result), status = 200, safe=False)
    else:
        return HttpResponse(status = 403)

def get_item_info(request):
    if request.method == "GET":
        result = {}
        base_items = []
        upper_items = UpperItem.objects.all().exclude(item_apiName__contains = 'TFT6_')
        upper_result = []
        for it in upper_items:
            upper_base = []
            for b in it.base_items.all():
                upper_base.append(b.item_id)
            data = {
                'id':it.item_id,
                'name':it.item_name,
                'img':it.item_img,
                'info':it.item_info,
                'apiName':it.item_apiName,
                'effect':it.item_effect,
                'baseItems':upper_base
            }
            upper_result.append(data)
        base_item_list = BaseItem.objects.all().values()
        for base in base_item_list:
            if base['item_name'] in specific_item:
                data = {
                    'id':base['item_id'],
                    'name':base['item_name'],
                    'img':base['item_img'],
                    'info':base['item_info'],
                    'apiName':base['item_apiName'],
                    'effect':base['item_effect']
                }
                base_items.append(data)
        if upper_items.exists():
            upper_result = list(upper_result)
            base_items = list(base_items)
            result = {'upper_items': upper_result, 'base_items': base_items}
            print(result)
            return JsonResponse(result, status = 200, safe=False)
        else:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=403)

def get_augment_info(request):
    if request.method == "GET":
        augments = Augment.objects.all()
        result = []
        for augment in augments:
            data = {
                'name':augment.augment_name,
                'apiName':augment.augment_apiName,
                'img': augment.augment_img,
                'effect':augment.augment_effect,
                'info':augment.augment_info,
                'id':augment.augment_id
            }
            result.append(data)
        return JsonResponse(list(result), status = 200, safe=False)
    else:
        return HttpResponse(status = 403)

def get_trait_detail(request, trait_id):
    if request.method == "POST":
        try:
            trait = Trait.objects.get(id = trait_id)
            data = {
                'name':trait.trait_name,
                'apiName':trait.trait_apiName,
                'img': trait.trait_img,
                'effect':trait.trait_effect['effect'],
                'info':trait.trait_info,
                'id':trait.id
            }
            return JsonResponse(list(data), status = 200, safe=False)
        except:
            return HttpResponse(status = 404)
    else:
        return HttpResponse(status = 403)
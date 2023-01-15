from django.shortcuts import render
from .models import Trait, UpperItem, BaseItem, Champion, Augment
from django.http import HttpResponse, JsonResponse
import json

specific_item = ['영혼의 형상','죽음의 저항','영원한 겨울', '무한한 삼위일체', '마나자네', '흑요석 양날 도끼', '란두인의 성소', '로켓 주먹', '황금 징수의 총', '존야의 역설', '우르프 천사의 지팡이', '축복받은 피바라기', '푸른 축복', '장미가시 조끼', '선의의 성배', '빛나는 죽음의 검', '용의 의지', '철갑의 서막', '수호상 돌갑옷', '악마 학살자', '새벽의 서광', '구인수의 심판', '공정의 주먹', '마법공학 생명검', '천공의 대검', '집단 충격기', '눈부신 건틀릿', '영겁의 속삭임', '타곤 정상의 펜던트', '엔젤로노미콘', '반짝이는 수은', '라바돈의 초월한 죽음모자', '고속 광자포', '면죄', '루난의 폭풍', '경외의 장막', '히라나의 창', '스태틱의 호의', '태양빛 망토', '장난꾸러기의 장갑', '거인의 맹세', '의지파괴자', '워모그의 자부심', '지크의 조화', '겨울바람', '즈롯 소환문', '메카 선택기', '에이스 상징', '방패대 상징', '톱날 피바라기', '싸움꾼 상징', '주문투척자 상징', '민간인 상징', '특등사수 상징', '엄호대 상징', '메카: 프라임 상징', '기계유망주 상징', '과부하_오류 // 거인 학살자', '해커 상징', '비결정적 정의의 손길', '자화 이온 충격기', '익살꾼 상징', '용수철이 든 고속 연사포', '정찰단 상징', '날뛰는 쇼진의 창', '더 고요한 침묵의 장막', '별 수호자 상징', '과열된 태양불꽃 망토', '지하세께 상징', '유도집전형 워모그의 갑옷', 'B.F. 대검', '곡궁', '쇠사슬 조끼', '음전자 망토', '쓸데없이 큰 지팡이', '여신의 눈물', '거인의 허리띠', '연습용 장갑', '뒤집개']
specific_upper_item = ['대천사의 지팡이', '피바라기', '덤불 조끼',  '힘의 성배', '죽음의 검', '용의 발톱', '전략가의 왕관', '수호자의 맹세', '가고일 돌갑옷', '밤의 끝자락', '구인수의 격노검', '마법공학 총검', '무한의 대검', '이온 충격기', '보석 건틀릿', '최후의 속삭임', '강철의 솔라리 펜던트', '거인 학살자', '모렐로노미콘', '방패파괴자', '수은', '라바돈의 죽음모자', '고속 연사포', '태양불꽃 망토', '구원', '루난의 허리케인',  '푸른 파수꾼', '침묵의 장막', '쇼진의 창', '스태틱의 단검', '도적의 장갑', '즈롯 차원문', '거인의 결의', '정의의 손길', '워모그의 갑옷', '지크의 전령', '서풍']
specific_augment = ['전투 마법사 I', '천상의 축복 I', '사이버네틱 이식술 I', '사이버네틱 외피 I', '사이버네틱 통신 I', '추방자 I', '단결된 의지 I', '고전압 I', '경량급 I', '응급처치 키트', '예견 I', '아이템 꾸러미 I', '루덴의 메아리 I','임시변통 방어구 I', '나이프의 날 I', '대격변 생성기', '재생의 바람 I', '사냥의 전율 I', '꼬마 거인', '3에 깃든 힘 I', '자리 비움', '도둑 무리 I', '커다란 친구 I', '일관성', '후반 전문가', '판도라의 대기석', '준비 I', '자동방어체계 심장', '방패대 심장', '동물특공대 심장', '싸움꾼 심장', '주문투척자 심장', '특등사수 심장', '엄호대 심장', '결투가 심장', '해커 심장', '선의 심장', '레이저단 심장','마스코트 심장', '황소부대 심장', '정찰단 심장', '무법자 심장', '별 수호자 심장']
specific_augment2 = ['방패대 문장', '지하세계 심장', '초월', '전투 마법사 II', '계산된 패배', '천상의 축복 II','맑은 정신', '재료 꾸러미', '사이버네틱 이식술 II', '사이버네틱 외피 II', '사이버네틱 통신 II', '추방자 II', '단결된 의지 II', '고전압 II', '경량급 II', '수완가', '보석 연꽃', '루덴의 메아리 II', '임시변통 방어구 II', '나이프의 날 II', '대사 촉진제', '휴대용 대장간', '부익부', '부익부+', '재활용 쓰레기통', '재생의 바람 II', '태양불꽃판', '허수아비 전선', '삼총사', '사냥의 전율 II', '고대의 기록 보관소 I', '교환의 장', '교환의 장+', '다른 태생 II', '3에 깃든 힘 II', '곱빼기', '문제가 두 배 II', '커다란 친구 II', '전투 훈련', '어수선한 마음', '응급처치 키트 II', '최후의 저항', '준비 II', '조준경 부착 I', '우르프의 꾸러미 I', '자동방어체계 문장', '에이스 문장', '동물특공대 문장', '싸움꾼 문장', '주문투척자 문장', '민간인 문장', '특등사수 문장', '엄호대 문장', '결투가 문장', '메카: 프라임 문장', '기계유망주 심장', '해커 문장', '선의 문장', '레이저단 문장', '마스코트 문장', '황소부대 문장', '익살꾼 문장', '정찰단 문장', '무법자 문장', '별 수호자 문장', '우세 심장', '위협 레벨: 최대']
specific_augment3 = ['도둑 무리 II', '전투 마법사 III', '이중 공중 보급', '천상의 축복 III', '사이버네틱 이식술 III', '사이버네틱 외피 III', '사이버네틱 통신 III', '단결된 의지 III', '고전압 III', '경량급 III', '신병', '예견 II', '황금 티켓', '큰손', '아이템 꾸러미 II', '루덴의 메아리 III', '나이프의 날 III', '찬란한 유물', '진보의 행진', '황금 알', '현명한 소비', '다른 태생 III', '3에 깃든 힘 III', '문제가 두 배 III', '신록의 장막', '뜻밖의 횡재', '뜻밖의 횡재+', '뜻밖의 횡재++', '숲의 부적', '생일 선물', '저주받은 왕관', '간이 대장간', '행운의 장갑', '준비 III', '잔혹한 계약', '빠른 판단', '고대의 기록 보관소 II', '우르프의 꾸러미 II', '자동방어체계 왕관', '에이스 왕관', '방패대 왕관', '동물특공대 왕관', '싸움꾼 왕관', '주문투척자 왕관', '민간인 왕관', '특등사수 왕관', '엄호대 왕관', '결투가 왕관', '메카: 프라임 왕관', '기계유망주 영혼', '해커 왕관', '선의 왕관', '레이저단 왕관', '마스코트 왕관', '황소부대 왕관', '익살꾼 왕관', '정찰단 왕관', '무법자 왕관', '별 수호자 왕관', '우세 영혼', '지하세계 영혼']

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
        upper_item_list = UpperItem.objects.all()
        upper_items = []
        for u in upper_item_list:
            if u.item_name in specific_upper_item:
                upper_items.append(u)
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
        if len(upper_items)!=0:
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
        augment_list = []
        augments = Augment.objects.all()
        for a in augments:
            if a.augment_name in specific_augment:
                augment_list.append(a)
        for a in augments:
            if a.augment_name in specific_augment2:
                augment_list.append(a)
        for a in augments:
            if a.augment_name in specific_augment3:
                augment_list.append(a)
        result = []
        for augment in augment_list:
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
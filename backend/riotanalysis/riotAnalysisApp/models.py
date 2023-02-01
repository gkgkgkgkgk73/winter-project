from django.db import models

#특성 기본 정보
class Trait(models.Model):
    trait_name = models.CharField(max_length=200, blank=True, null=True, )
    trait_apiName = models.CharField(max_length=200 ,blank=True, null=True, )
    trait_img = models.CharField(max_length=200, blank=True, null=True, )
    trait_effect = models.JSONField()
    trait_info = models.CharField(max_length=1000, blank=True, null=True, )
    
class Augment(models.Model):
    augment_apiName= models.CharField(max_length=200, blank=True, null=True,)
    augment_info = models.CharField(max_length=200, blank=True, null=True,)
    augment_img = models.CharField(max_length=200, blank=True, null=True, )
    augment_id = models.IntegerField()
    augment_name = models.CharField(max_length=200, blank=True, null=True, )
    augment_effect = models.JSONField()
#챔피언 기본 정보
class Champion(models.Model):
    champion_apiName = models.CharField(max_length=300, blank=True, null=True, )
    champion_variables = models.JSONField()
    champion_name = models.CharField(max_length=200, blank=True, null=True, )
    champion_img = models.CharField(max_length=200, blank=True, null=True, )
    champion_info = models.CharField(max_length=1000, blank=True, null=True, )
    traidels.ManyToManyField(
        Trait,
        related_name='trait'
    )
    champion_stats = models.JSONField()
    champion_cost = models.IntegerField()
    
#조합 아이템 정보
class BaseItem(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=200,blank=True, null=True, )
    item_img = models.CharField(max_length=200, blank=True, null=True, )
    item_info = models.CharField(max_length=1000, blank=True, null=True, default='')
    item_apiName = models.CharField(max_length=200,blank=True, null=True, )
    item_effect = models.JSONField()
    
#완성 아이템 및 오른 아이템 정보
class UpperItem(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=200,blank=True, null=True, )
    item_img = models.CharField(max_length=200, blank=True, null=True, )
    item_info = models.CharField(max_length=1000, blank=True, null=True, default='')
    item_apiName = models.CharField(max_length=200,blank=True, null=True, )
    item_effect = models.JSONField()
    base_items = models.ManyToManyField(
        BaseItem,
        related_name = 'base_item'
    )

class MatchData(models.Model):
    match_id = models.CharField(max_length=100,blank=True)
    puuid = models.CharField(max_length=1000,blank=True)
    game_type = models.CharField(max_length=1000,blank=True)
    set_number = models.IntegerField(default = 0)
    last_level = models.IntegerField()
    placement = models.IntegerField()
    last_round = models.IntegerField()
    play_time = models.FloatField()
    gold_left = models.IntegerField()
    total_damage_to_players = models.IntegerField()

    augments1 = models.CharField(max_length= 100,blank=True)
    augments2 = models.CharField(max_length= 100,blank=True)
    augments3 = models.CharField(max_length= 100,blank=True)

    traits = models.JSONField()
    units = models.JSONField()
    
class ItemStat(models.Model):
    champion_name = models.CharField(max_length=100,blank=True)
    item_name = models.CharField(max_length=100,blank=True)
    pick_count = models.IntegerField()
    win_count = models.IntegerField()
    pick_rate = models.FloatField()
    win_rate = models.FloatField()


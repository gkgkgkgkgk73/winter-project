from django.db import models

#특성 기본 정보
class Trait(models.Model):
    trait_name = models.CharField(max_length=200)
    trait_img = models.ImageField(upload_to= 'gameimages/', blank=True,default='')
    trait_champions_name = models.CharField(max_length=200)
    trait_info = models.CharField(max_length=1000)
    
#챔피언 기본 정보
class Champion(models.Model):
    champion_name = models.CharField(max_length=200)
    champion_img = models.ImageField(upload_to='gameimages/', blank=True, default='')
    champion_info = models.CharField(max_length=1000)
    traits = models.ManyToManyField(
        Trait,
        related_name='trait'
    )
    champion_cost = models.IntegerField()
    
#조합 아이템 정보
class BaseItem(models.Model):
    item_name = models.CharField(max_length=200)
    item_img = models.ImageField(upload_to='gameimages/', blank=True, default='')
    item_info = models.CharField(max_length=1000)
    
#완성 아이템 및 오른 아이템 정보
class UpperItem(models.Model):
    item_name = models.CharField(max_length=200)
    item_img = models.ImageField(upload_to='gameimages/', blank=True, default='')
    item_info = models.CharField(max_length=1000)
    base_items = models.ManyToManyField(
        BaseItem,
        related_name = 'base_item'
    )

class MatchData(models.Model):
    match_id = models.CharField(max_length=100,blank=True)
    puuid = models.CharField(max_length=1000,blank=True)
    last_level = models.IntegerField()
    placement = models.IntegerField()
    last_round = models.IntegerField()
    play_time = models.FloatField()
    gold_left = models.IntegerField()
    total_damage_to_players = models.IntegerField()

    augments = models.JSONField()
    traits = models.JSONField()
    units = models.JSONField()
    

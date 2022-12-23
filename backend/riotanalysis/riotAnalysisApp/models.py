from django.db import models
from django.contrib.postgres.fields import ArrayField


#특성 기본 정보
class Trait(models.Model):
    trait_name = models.CharField(max_length=200)
    trait_img = models.ImageField(upload_to= 'gameimages/', blank=True,default='')
    trait_champions_name = ArrayField(models.CharField(max_length=200), blank=True)
    trait_info = models.CharField(max_length=1000)
    
#챔피언 기본 정보
class Champion(models.Model):
    champion_name = models.CharField(max_length=200)
    champion_img = models.ImageField(upload_to='gameimages/', blank=True, default='')
    champion_info = models.CharField(max_length=1000)
    traits = ArrayField(models.CharField(max_length=200))
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
    base_items = ArrayField(models.ForeignKey(
        BaseItem,
        on_delete=models.CASCADE,
        null=True,
        related_name = 'base_item'
    ))
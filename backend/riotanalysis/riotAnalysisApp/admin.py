""" import module """
from django.contrib import admin
# from django.contrib.admin.views.main import ChangeList
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from .models import Trait, UpperItem, BaseItem, Champion, MatchData, ItemStat

admin.site.register(MatchData)
admin.site.register(BaseItem)
admin.site.register(UpperItem)
admin.site.register(Champion)
admin.site.register(Trait)
admin.site.register(ItemStat)
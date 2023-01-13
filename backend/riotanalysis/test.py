import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")
import django
django.setup()
from riotanalysisapp.models import BaseItem, UpperItem

a = BaseItem.objects.all().values('item_id', 'item_name')
print(a[0])
b = UpperItem.objects.all().values('item_id', 'item_name')
print(b[0])
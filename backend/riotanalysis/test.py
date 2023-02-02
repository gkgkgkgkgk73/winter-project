import os
import json
import pandas as pd
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")
import django
django.setup()
from riotanalysisapp.models import MatchData
from django.db.models import Q
import matplotlib.pyplot as plt

def get_champion_win_rate(champion_name):
    queryset = MatchData.objects.all().values()
    game_size = len(queryset)

    win_count = 0
    pick_count = 0

    for query in queryset:
        placement = query['placement']
            
        units = json.loads(query['units'])
        for unit in units:
            if unit['character_id'] != champion_name:
                pass
            else:
                pick_count += 1
                if placement < 5:
                    win_count += 1
    win_rate = 0
    if pick_count > 0:
        win_rate = win_count / pick_count
    return [round(win_rate * 100, 2), round(pick_count/game_size * 100, 2)]
print(get_champion_win_rate('TFT8_Jax'))
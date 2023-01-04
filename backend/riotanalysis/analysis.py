import os
import json
import pandas as pd
import requests
from pathlib import Path
import time

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","riotanalysis.settings")

import django
django.setup()
from riotanalysisapp.models import MatchData

df = MatchData.objects.values('last_level')
last_levels = []
for level in df:
    last_levels.append(level['last_level'])

df = MatchData.objects.values('placement')
top4 = []
for place in df:
    rank = place['placement']
    istop4 = 0
    if rank > 4:
        istop4 = False
    else:
        istop4 = True
    top4.append(istop4)


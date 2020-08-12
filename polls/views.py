from django.http import HttpResponse
from .models import PackContent, Pack
import json
def getAllPacks(r):
    packs = Pack.objects.all()
    packsJson = {"packs": {}}
    for pack in packs:
        packsJson["packs"][pack.packId] = pack.title

    return HttpResponse(json.dumps(packsJson))
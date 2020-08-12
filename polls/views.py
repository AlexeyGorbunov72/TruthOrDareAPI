from django.http import HttpResponse, JsonResponse
from .models import PackContent, Pack
import json
def getAllPacks(r):
    packs = Pack.objects.all()
    packsJson = {"packs": {}}
    for pack in packs:
        packsJson["packs"][pack.packId] = pack.title

    return HttpResponse(json.dumps(packsJson))

def getPackContent(r, packId):
    packs = PackContent.objects.filter(packId=packId)
    packsJson = {"pack": []}
    for pack in packs:
        packsJson["pack"].append({"task": {"levelOfHard": pack.levelOfHard,
                                  "content": pack.content,
                                  "isTruth": pack.isTruth}})

    return HttpResponse(json.dumps(packsJson))

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import PackContent, Pack
import json

@method_decorator(csrf_exempt, name='dispatch')
class MyViewClass(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view.csrf_exempt = True
        return view
def getAllPacks(r):
    packs = Pack.objects.all()
    packsJson = {"packs": []}
    for pack in packs:
        packsJson["packs"].append({"id": pack.packId,
                                   "title": pack.title,
                                   "levelAction": pack.levelAction,
                                   "levelTruth": pack.levelTruth})

    return HttpResponse(json.dumps(packsJson))


def getPackContent(r, packId):
    packs = PackContent.objects.filter(packId=packId)
    packsJson = {"pack": []}
    for pack in packs:
        packsJson["pack"].append({"levelOfHard": str(pack.levelOfHard),
                                  "content": pack.content,
                                  "isTruth": pack.isTruth})

    return HttpResponse(json.dumps(packsJson))

@csrf_exempt
def loadPack(request, **kwargs):
    tasksUser = json.loads(request.body.decode())['tasks']
    packUser = json.loads(request.body.decode())['pack']

    pack = Pack()
    pack.levelTruth = packUser["levelTruth"]
    pack.levelAction = packUser["levelAction"]
    pack.title = packUser["title"]
    pack.save()
    newId = pack.packId
    for taskUser in tasksUser:
        task = PackContent()
        task.packId = newId
        task.levelOfHard = float(taskUser["levelOfHard"])
        task.content = taskUser["content"]
        task.isTruth = taskUser["isTruth"]
        task.save()
    return HttpResponse("ok")
loadPack.csrf_exempt = True
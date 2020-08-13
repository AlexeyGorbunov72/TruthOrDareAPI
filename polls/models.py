from django.db import models
class Pack(models.Model):
    packId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    levelTruth = models.CharField(max_length=200, default='5')
    levelAction = models.CharField(max_length=200, default='5')
    def __str__(self):
        return f"{self.packId}| {self.title}"

class PackContent(models.Model):
    content = models.CharField(max_length=500)
    packId = models.IntegerField()
    isTruth = models.IntegerField()
    levelOfHard = models.IntegerField()
    def __str__(self):
        return f"{self.packId}| {self.content}"

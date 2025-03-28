from django.db import models

class QueueType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.IntegerField()


class Counter(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    queue_type = models.ForeignKey(QueueType, on_delete=models.CASCADE)

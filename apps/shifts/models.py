from django.db import models

class Turn(models.Model):
    turn_number = models.CharField(max_length=10)
    customer = models.ForeignKey('clients.Clients', on_delete=models.CASCADE)
    employee = models.ForeignKey('user.Employee', on_delete=models.SET_NULL, null=True, blank=True)
    counter = models.ForeignKey('counters.Counter', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20)
    queue_type = models.ForeignKey('counters.QueueType', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    assigned_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)


class TurnLog(models.Model):
    turn = models.ForeignKey(Turn, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    previous_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    system_user = models.CharField(max_length=50)
    notes = models.TextField()

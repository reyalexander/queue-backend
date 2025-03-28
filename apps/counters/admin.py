from django.contrib import admin
from .models import Counter, QueueType

admin.site.register(QueueType)
admin.site.register(Counter)
from django.db import models


class Note(models.Model):
    label = models.CharField(max_length=120)
    text = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
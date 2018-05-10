from django.db import models


class Paste(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    language = models.CharField(max_length=50, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    

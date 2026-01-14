from django.db import models

# Create your models here.

from django.db import models

class Message(models.Model):
	name = models.CharField(max_length=255)
	datetime = models.CharField(max_length=255)
	text = models.CharField(max_length=255)

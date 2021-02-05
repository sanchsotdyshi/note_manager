from django.db import models

# Create your models here.
class Note(models.Model):
	header = models.CharField(max_length=30)
	content = models.CharField(max_length=100)

	def __str__(self):
		return self.header
from django.db import models

class SongCi(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=20)
	content = models.CharField(max_length=200)
	def __str__(self):
		return self.title

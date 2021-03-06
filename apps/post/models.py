from django.db import models
from lib import constants as const
from apps.taxonomy.models import Category, Tag

class Post(models.Model):
	title = models.CharField(max_length=const.POST_TITLE_MAX_LENGTH)
	description = models.TextField()
	category = models.ForeignKey(
		Category, on_delete=models.SET_NULL, null=True, blank=True
	)
	tag = models.ManyToManyField(Tag)
	image = models.ImageField(upload_to=const.IMAGE_UPLOAD_PATH)

	def __str__(self):
		return self.title

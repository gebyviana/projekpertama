from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

		
class Post(models.Model):
	categories_choices = (
		('appetizer', 'Appetizer'),
		('main_course', 'Main Course'),
		('dessert', 'Dessert')
	)

	author = models.ForeignKey(User)
	categories = models.CharField(max_length=20, choices=categories_choices)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#Creating User Table for getting the data about users.
@python_2_unicode_compatible
class User(models.Model):
	user_id = models.CharField(max_length=320)
	gcm_id  = models.CharField(max_length=320)

	def __str__(self):
		return self.user_id
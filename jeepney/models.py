from django.db import models
from django.core.urlresolvers import reverse

class Jeep(models.Model):
	route= models.CharField(max_length=200)
	place= models.CharField(max_length=900)
	updated= models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp= models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.route
	def __str__(self):
		return self.route

	def get_absolute_url(self):
		return reverse("detail", kwargs={"id": self.id})
		#return "/jeepney/%s" %(self.id)
# Create your models here.

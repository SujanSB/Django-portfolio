from django.db import models

# Create your models here.
class About(models.Model):
	description = models.TextField()
	image = models.ImageField(upload_to ="about")

	def __str__(self):
		return "About Myself"


class Service(models.Model):
	name= models.CharField(max_length=30,verbose_name="My Services")
	image = models.ImageField(upload_to ="Service")

	
	def __str__(self):
		return self.name

class SelectedWorks(models.Model):
	title =models.CharField(max_length=50,verbose_name="My works" )
	description =models.TextField(max_length=200)
	link=models.CharField(max_length=80)
	image=models.ImageField(upload_to="works")

	def __str__(self):
		return self.title



from django.db import models
from django.utils import timezone

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



class blogHaru(models.Model):
	
	blog_category = [
		('Programming', 'Programming'),
		('Travel', 'Travel'),
		('Techlology', 'Techlology'),
		('Motivation', 'Motivation'),
		('Others', 'Others')
	]
	category = models.CharField(max_length=15, choices=blog_category)
	title = models.CharField(max_length=200)
	# subtitle = models.CharField(max_length=200)
	description=models.TextField()
	image = models.ImageField(upload_to='Blog_images')
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		super(blogHaru, self).save(*args, **kwargs)


		
class Contact(models.Model):
	name =models.CharField(max_length=50 )
	email= models.EmailField()
	message=models.TextField(max_length=300)
	
	
	def __str__(self):
		return self.name

from email.mime import image, message
import numbers
from pyexpat import model
from django.db import models

# Create your models here.

class Userprofile(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField(null=True)
    description = models.TextField()
    address = models.CharField( max_length=50)
    image = models.ImageField( upload_to="images")
    
    def __str__(self):
        return self.first_name
    
class Skill(models.Model):
    name =models.CharField( max_length=50)
    persent = models.IntegerField()
    bar = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Skills'
    

    
class Services(models.Model):
    title = models.CharField( max_length=50)
    description= models.TextField()
    i_class = models.CharField( max_length=50)
    
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Services'


class Tags(models.Model):
    name = models.CharField( max_length=50)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tags'
    
            
class Portfolios(models.Model):
    title = models.CharField( max_length=50)
    image = models.ImageField( upload_to="images" )
    image_slide = models.ImageField( upload_to="images")
    image_slide2 = models.ImageField( upload_to="images")
    category       = models.ManyToManyField(Tags) 
    project_url = models.CharField( max_length=50, null= True, blank=True)
    project_client = models.CharField( max_length=50, null= True, blank=True)
    date_created   = models.DateTimeField( auto_now_add=True)
    description    =models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Portfolio'
        

 
    
class ContactForm(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( )
    phone = models.IntegerField()
    subject = models.CharField( max_length=50)
    message = models.TextField()
    date_created   = models.DateTimeField( auto_now=True)
    def __str__(self):
        return self.name
    
    
class Achievements(models.Model):
    numbers = models.IntegerField()
    description = models.TextField()
    i_class = models.CharField( max_length=50)
    
    def __str__(self):
        return f'year:{self.numbers} description{self.description.lower()[:30]}'
    
    class Meta:
        verbose_name_plural = 'Achievments'
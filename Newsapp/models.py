from django.db import models

# Create your models here.
class News11(models.Model):
    Article_datetime = models.DateTimeField(default=datetime.now, blank=True)
    Article_name = models.CharField(max_length=100)
    Article_author= models.CharField(max_length=50)
    Article_image_name= models.CharField(max_length=30)
    Article_image = models.ImageField(upload_to='images/')
    Article_video = models.FileField(upload_to='videos/',null=True)
    Article_here = models.CharField(max_length=1500)


    def __str__(self):
        return self.(Article_name,Article_here)

""" User model already available in django
class user(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    password = CharField(max_length=20)
    confirm_password = CharField(max_length=20)  """

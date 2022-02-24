from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.



class About(models.Model):
    name = models.CharField(max_length=50)
    about_text = RichTextUploadingField()
    
    def __str__(self):
        return self.about_text



class Login(models.Model):
    name = models.CharField(max_length=50)
    login_text = RichTextUploadingField()
    
    def __str__(self):
        return self.name


    
class Signup(models.Model):
    name = models.CharField(max_length=50)
    sign_up_text = RichTextUploadingField()
    
    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Service(models.Model):
    img = models.ImageField(upload_to='images/')
    loyiha_haqida = models.CharField(max_length=255)
    prospotr = models.CharField(max_length=5)
    time = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return self.loyiha_haqida
    
class Blog(models.Model):
    img = models.ImageField(upload_to='images/')
    blog_mavzusi = models.CharField(max_length=30)
    post_haqida = models.CharField(max_length=150)


    def __str__(self):
        return self.blog_mavzusi

class Comment(models.Model):
    user_name = models.CharField(max_length=25)
    img = models.ImageField(upload_to='images')
    user_comment = models.CharField(max_length=125)
    time = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.user_name

class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    message =  models.TextField()

    def __str__(self):
        return self.name
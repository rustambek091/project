from django.db import models

# Create your models here.
class abouts(models.Model):
    title = models.CharField(max_length=25)
    img = models.ImageField(upload_to='images/')
    mavzu = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class servicess(models.Model):
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
from django.db import models  
  
# Create your models here.  
  
class Article(models.Model):
    title = models.CharField(max_length=200)
    article_text = models.CharField(max_length=500)
    photos = models.ImageField(upload_to='article_photos/')
    location = models.CharField(max_length=100)
    event_date = models.DateField()

    def __str__(self):
        return self.title


class Service(models.Model):
    service_name = models.CharField(max_length=200)
    service_description = models.CharField(max_length=500)  # Changed to CharField
    bootstrap_icon = models.CharField(max_length=50)

    def __str__(self):
        return self.service_name
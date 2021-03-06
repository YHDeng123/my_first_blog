from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


class Category (models.Model):
    name = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name
      
class Article(models.Model):
    
    category = models.ForeignKey('Category', blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    
        
        
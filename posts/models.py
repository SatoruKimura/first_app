from django.db import models
# Create your models here.
from django.utils import timezone 

class Post(models.Model):
  class Meta:
    db_table = 'posts'

  content= models.CharField(blank=True)
  created_at = models.DateTimeField(default=timezone.now)

from django.db import models

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    timeStamp=models.DateTimeField(null=True,blank=True)
    content=models.TextField()
    slug=models.CharField(max_length=130)
    
    def __str__(self):
        return self.title + " by " + self.author
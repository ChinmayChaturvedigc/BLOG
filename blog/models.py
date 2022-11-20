import email
from django.db import models

class Contact (models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 225)
    email = models.CharField( max_length = 225)
    content = models.TextField( max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email
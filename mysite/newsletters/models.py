from django.db import models

# Create your models here.
class Registered(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    # Python 2 
    # def __unicode__(self):
    #     return self.name
    
    def __str__(self):
        return self.email
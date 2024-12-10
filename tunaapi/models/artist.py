from django.db import models
# testsss

class Artist(models.Model):

    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    bio = models.CharField(max_length=50)
    
    

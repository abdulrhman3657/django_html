from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class note(models.Model):
    noteName = models.CharField(max_length=300)
    noteContent = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.noteName
    

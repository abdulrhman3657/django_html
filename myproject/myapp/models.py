from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# every model is mapped to a single database table

class note(models.Model):
    noteName = models.CharField(max_length=300)
    noteContent = models.TextField()

    # default=timezone.now: take the time from another module
    # auto_now=True: update the date with each edit
    # auto_now_add=True: set the time only when the object is created
    date_created = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)


    # make the object name more discriptive
    #ex: my first post instead of object 1, see note.objects.all()
    def __str__(self):
        return self.noteName
    
from django.contrib import admin
from . import models

# add note class to admin page
admin.site.register(models.note)

# Register your models here.

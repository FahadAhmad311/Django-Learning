from django.contrib import admin

# Register your models here.
from .models import College
from .models import Principal
from .models import Subject
from .models import Teacher

#Here i have to register models which i have created in App directory models.py
admin.site.register(College)
admin.site.register(Principal)
admin.site.register(Subject)
admin.site.register(Teacher)
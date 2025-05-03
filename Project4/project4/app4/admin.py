from django.contrib import admin
from .models import Subject
from .models import Teacher
from .models import College
from .models import Principal
# Register your models here.
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(College)
admin.site.register(Principal)
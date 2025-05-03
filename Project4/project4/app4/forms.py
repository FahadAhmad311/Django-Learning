from django import forms
from .models import Subject
from .models import Teacher
from .models import Principal
from .models import College

class LogSubject(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

class LogTeacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__" 
        
class LogPrincipal(forms.ModelForm):
    class Meta:
        model = Principal
        fields = "__all__" 
        
class LogCollege(forms.ModelForm):
    class Meta:
        model = College
        fields = "__all__"                      
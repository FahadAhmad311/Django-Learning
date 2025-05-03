from django.urls import path
from .import views

urlpatterns = [
    path('college/', views.viewCollege, name="College"),
    path('principal/', views.viewPrincipal, name="Principal"),
    path('subject/', views.viewSubject, name="Subject"),
    path('teacher/', views.viewTeacher, name="Teacher")
]

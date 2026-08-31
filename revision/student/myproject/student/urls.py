from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('student_list/', views.student_list, name='student-list'),
    path('contact/', views.contact, name='contact'),
    path('api/student/', views.student_api)
]
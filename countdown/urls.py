from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('event/', views.event_detail, name='event'), 
]
"""
The user urls
custom made urls
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('event/', views.event_detail, name='event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),   
]

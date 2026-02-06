from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscriber, name='subscriber'),
    path('newsletter/', views.send_newsletter, name='send_newsletter'),
]
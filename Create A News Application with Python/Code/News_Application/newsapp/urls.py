from django.urls import path
from newsapp import views

urlpatterns = [
    path('home/',views.home,name='home'),
]

from django.urls import path
from . import views

app_name = 'dragons'

urlpatterns = [
    path('',views.index, name='index'),
    path('calculate',views.calculate, name='calculate'),
]
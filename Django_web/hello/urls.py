from django.urls import path
from . import views

app_name = 'hello'
urlpatterns = [
    path('', views.index, name='hello_index'),
    path('index2', views.index2, name='index2')
]

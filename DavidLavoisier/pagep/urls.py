from django.urls import path
from . import views

app_name = 'pagep'
urlpatterns = [
    path('', views.index, name="index"),
]
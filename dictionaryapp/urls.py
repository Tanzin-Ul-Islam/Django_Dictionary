from django.urls import path
from . import views
app_name = 'dictionaryapp'
urlpatterns = [
    path('', views.index, name="index"),
]

from django.urls import path
from .views import MyAPIVIewEven, MyAPIVIewOdd
app_name = "articles"

urlpatterns = [
    path('even', MyAPIVIewEven.as_view()),
    path('odd', MyAPIVIewOdd.as_view()),
]

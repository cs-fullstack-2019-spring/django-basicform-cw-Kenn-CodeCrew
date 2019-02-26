from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("welcome/", views.welcome, name="welcome"),
    path("<int:accountID>/add5/", views.add5, name="add5"),
]
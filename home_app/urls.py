from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path("home/light", views.light_home, name="light_home"),
    path("home/dark", views.dark_home, name="dark_home"),
]

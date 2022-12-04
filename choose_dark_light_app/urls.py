from django.urls import path
from . import views

app_name = "choose_dark_light_app"

urlpatterns = [
    path("", views.choose, name="choose"),
]

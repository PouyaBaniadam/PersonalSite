from django.shortcuts import render
from contact_me_app.models import Message, SocialMedia
from projects_app.models import *
from .models import *


def light_home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("message")
        Message.objects.create(name=name, email=email, number=number, message=message)

    programming_experience_datas = ProgrammingExperience.objects.all()
    other_experience_datas = OtherExperience.objects.all()
    about_me_datas = AboutMe.objects.last()
    experiences_and_stuff = ExperienceAndAchievements.objects.all()
    social_medias = SocialMedia.objects.last()
    project_datas = Project.objects.all()

    return render(request, "home_app/light.html",
                  context={"programming_experience_datas": programming_experience_datas,
                           "other_experience_datas": other_experience_datas, "about_me_datas": about_me_datas,
                           "experiences_and_stuff": experiences_and_stuff, "social_medias": social_medias,
                           "project_datas": project_datas})


def dark_home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("message")
        Message.objects.create(name=name, email=email, number=number, message=message)

    programming_experience_datas = ProgrammingExperience.objects.all()
    other_experience_datas = OtherExperience.objects.all()
    about_me_datas = AboutMe.objects.last()
    experiences_and_stuff = ExperienceAndAchievements.objects.all()
    social_medias = SocialMedia.objects.last()
    project_datas = Project.objects.all()

    return render(request, "home_app/dark.html",
                  context={"programming_experience_datas": programming_experience_datas,
                           "other_experience_datas": other_experience_datas, "about_me_datas": about_me_datas,
                           "experiences_and_stuff": experiences_and_stuff, "social_medias": social_medias,
                           "project_datas": project_datas})

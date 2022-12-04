from django.shortcuts import render

from home_app.models import AboutMe


def choose(request):
    website_name = AboutMe.objects.last()
    return render(request, 'choose_dark_light_app/choose_dark_light.html', context={"website_name": website_name})

from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    number = models.CharField(max_length=13)
    message = models.TextField(max_length=5000)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    telegram = models.URLField(max_length=100)
    instagram = models.URLField(max_length=100)
    github = models.URLField(max_length=100)

    def __str__(self):
        return "Social media"

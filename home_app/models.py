from django.db import models


class AboutMe(models.Model):
    website_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    bio = models.TextField(max_length=100)
    birthday = models.CharField(max_length=10)
    age = models.CharField(max_length=2)
    home_image = models.ImageField(upload_to="Admin profile images")
    about_me_image = models.ImageField(upload_to="Admin profile images")
    address = models.CharField(max_length=150)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=11)
    university = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "About me"


class ProgrammingExperience(models.Model):
    title = models.CharField(max_length=50)
    percentage = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.percentage}"


class OtherExperience(models.Model):
    title = models.CharField(max_length=50)
    percentage = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.percentage}"


class ExperienceAndAchievements(models.Model):
    title = models.CharField(max_length=50)
    number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title} - {self.number}"

    class Meta:
        verbose_name_plural = "Experiences and achievements"

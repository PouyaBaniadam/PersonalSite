from django.db import models


class Project(models.Model):
    date = models.CharField(max_length=30)
    programmer = models.CharField(max_length=75)
    title = models.CharField(max_length=50)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="Projects images")
    file = models.FileField(upload_to="Projects files")

    def __str__(self):
        return self.title

# class ProjectImage(models.Model):
#     project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to="project images")
#
#     def __str__(self):
#         return self.project.title

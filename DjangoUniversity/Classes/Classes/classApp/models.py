from django.db import models


class DjangoClasses(models.Model):
    title = models.CharField(max_lenght=60)
    course_number = models.IntergerField()
    instructor = models.CharField(max_lenght=60)
    duration = models.FloatField()

    objects = models.Manager()

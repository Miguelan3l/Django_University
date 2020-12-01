from django.db import models


# Create your models here.

class djangoClasses(models.Model):
    Tittle = models.CharField(max_length=60)
    CourseNumber = models.IntegerField()
    Instructor = models.CharField(max_length=100, default="")
    Duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.Tittle


Student_1 = djangoClasses.objects.update_or_create(Tittle="Economics", CourseNumber=201, Instructor="Jackie Dunn",
                                            Duration=1.5)
Student_2 = djangoClasses.objects.update_or_create(Tittle="ART", CourseNumber=301, Instructor="Smith",
                                            Duration=2.5)
Student_3= djangoClasses.objects.update_or_create(Tittle="Sports", CourseNumber=401, Instructor="Ray Tanner",
                                            Duration=1.0)

### Abstract inheritance


from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    school = models.CharField(max_length=100)

class Teacher(CommonInfo):
    subject = models.CharField(max_length=100)



### Multi-table inheritance

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

class Student(Person):
    school = models.CharField(max_length=100)

class Teacher(Person):
    subject = models.CharField(max_length=100)



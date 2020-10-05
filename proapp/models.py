from django.db import models

class RegistrationData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)

class FeedbackData(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField()
    date = models.DateTimeField(max_length=50)
    feedback = models.CharField(max_length=200)

from multiselectfield import MultiSelectField

class ContactData(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=50)

    COURSES_CHOICES = (
        ('Python','PYTHON'),
        ('Django','DJANGO'),
        ('Ui','UI'),
        ('RestAPI','REST API')
    )
    courses = MultiSelectField(max_length=100,choices=COURSES_CHOICES)

    TRAINER_CHOICES = (
        ('Shubham','SHUBHAM'),
        ('Uttam','UTTAM'),
        ('Harun','HARUN')
    )
    trainers = MultiSelectField(max_length=50,choices=TRAINER_CHOICES)

    BRANCHES_CHOICES = (
        ('Pune','PUNE'),
        ('Mumbai','MUMBAI'),
        ('Hyd','HYDERABAD'),
        ('Bang','BANGALORE')
    )
    branches = MultiSelectField(max_length=50,choices=BRANCHES_CHOICES)
    date = models.DateField(max_length=50)
    gender = models.CharField(max_length=50)

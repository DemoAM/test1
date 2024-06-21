from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(unique=True)
    ROLE_CHOICES = (
        ('A', 'Admin'),
        ('S', 'Student'),
        ('T', 'Teacher'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='T')


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        rseults = super().get_queryset(*args, **kwargs)
        return rseults.filter(ROLE_CHOICES="S")


class Student(User):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    student = StudentManager


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)


class TeacherManager(BaseUserManager):
    def get_queryser(self, *args, **kwargs):
        rseults = super().get_queryset(*args, **kwargs)
        return rseults.filter(ROLE_CHOICES="T")

class Teacher(User):
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    teacher = TeacherManager


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

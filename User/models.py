import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    email = models.EmailField(unique=True)
    ROLE_CHOICES = (
        ("A", "Admin"),
        ("AU", "Author"),
        ("B", "Buyer"),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="B")


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="S")


class Buyer(User):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    objects = StudentManager()


class BuyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)


class AuthorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role="AU")


class AuthorUser(User):
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    objects = AuthorManager()


class AuthorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return self.title



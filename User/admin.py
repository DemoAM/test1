from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
    ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id"]


@admin.register(StudentProfile)
class StuProfile(admin.ModelAdmin):
    list_display = ["id"]

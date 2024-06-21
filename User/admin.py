from django.contrib import admin
from User.models import User
from User import models
admin.site.register(User)
admin.site.register(models.Book)
admin.site.register(models.Category)
admin.site.register(models.Author)


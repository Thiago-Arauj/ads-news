from django.contrib import admin
from apps.news import models

admin.site.register(models.Category)

admin.site.register(models.News)
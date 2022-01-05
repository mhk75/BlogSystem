from django.contrib import admin
from news.models import *

# Register your models here.


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

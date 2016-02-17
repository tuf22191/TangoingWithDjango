from django.contrib import admin 
from rango.models import Category, Page
from django.db import models


class CategoryClass(admin.ModelAdmin):
    list_display = ('name' ,'view', 'likes', 'slug')
    prepopulated_fields = {'slug':('name',)}



admin.site.register(Category, CategoryClass)
class PageClass(admin.ModelAdmin):
    list_display= ('category', 'title', 'url', 'views')

admin.site.register(Page, PageClass)



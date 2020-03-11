from django.contrib import admin
from articles.models import Blog, Category,Comment
# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Category)

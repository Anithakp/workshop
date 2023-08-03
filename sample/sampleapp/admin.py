from django.contrib import admin

from .models import destination, book

# Register your models here.
admin.site.register(destination)
admin.site.register(book)
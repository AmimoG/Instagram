from django.contrib import admin

from .models import Image, Comments, Profile

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comments)

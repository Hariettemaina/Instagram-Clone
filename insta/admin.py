from django.contrib import admin
from .models import posts,Profile,Likes,Comment

admin.site.register(posts)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Likes)
admin.site.register(Comment)
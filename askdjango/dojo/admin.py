from django.contrib import admin

# Register your models here.
from dojo.models import Post, GameUser


admin.site.register(Post)

admin.site.register(GameUser)
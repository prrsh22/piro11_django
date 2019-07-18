from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)


# make migrations를 통해 DB에 model 꼴의 데이터테이블 만듦
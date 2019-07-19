from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','created_at','updated_at']

#admin.site.register(Post) 여러 방법이 있음

# make migrations를 통해 DB에 model 꼴의 데이터테이블 만듦
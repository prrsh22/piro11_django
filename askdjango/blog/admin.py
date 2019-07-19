from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','content_size','created_at','updated_at']

    def content_size(self,post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

#admin.site.register(Post) 여러 방법이 있음

# make migrations를 통해 DB에 model 꼴의 데이터테이블 만듦
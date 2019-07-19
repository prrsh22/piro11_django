from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post,Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions=['make_published','make_draft']
    list_display=['id','title','content_size','status','created_at','updated_at']

    def content_size(self,post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

    def make_published(self,request,queryset):
        updated_count=queryset.update(status='p')
        self.message_user(request,'{}건의 포스팅을 Published 상태로 변경'.format(updated_count))

    def make_draft(self,request,queryset):
        updated_count=queryset.update(status='d')
        self.message_user(request,'{}건의 포스팅을 Draft 상태로 변경'.format(updated_count))

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
#admin.site.register(Post) 여러 방법이 있음

# make migrations를 통해 DB에 model 꼴의 데이터테이블 만듦
from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100,
          choices=(
        ('제목1','제목1 레이블'), #저장될 값, 보여질 값
        ('제목2','제목2 레이블'),
        ('제목3','제목3 레이블'),
    ), verbose_name='제목',help_text="제목을 고르시오") #길이 제한이 있는 문자열
    content=models.TextField(verbose_name="내용") #길이 제한이 없는 문자열
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

# DB에 맞는 표현 --> 그냥 python에서는 텍스트에 대해 길이 제한 없지만
# DB는 다르므로 TextField, CharField로 구분

#auto_now_add: 최초 생성시 시간 저장
#auto_now: 바뀔 때마다 시간 저장 (둘 다 자동. 입력 x)
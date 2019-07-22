from django.conf import settings
from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete='CASCADE',related_name='+')
    # related name='+' --> user.post_set.all() : 이거를 blog에 있는 user에 대해서만 사용할 수 있도록 양보
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
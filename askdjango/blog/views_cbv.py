from django.views.generic import CreateView
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'


class PostCreateView(CreateView):
    model=Post
    form_class=PostForm
    #원래는 success url 등록해야 함 (성공시 어디로 갈 것인지)


post_new=PostCreateView.as_view()
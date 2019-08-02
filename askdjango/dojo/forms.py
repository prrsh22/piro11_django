from django import forms

from dojo.models import Post





class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields='__all__'와 같음
        fields = ['title', 'content', 'user_agent']
        widgets = {
            'user_agent': forms.HiddenInput,
        }

'''
    def save(self, commit=True):
        self.instance = Post(**self.cleaned_data)
        if commit:
            self.instance.save()
        return self.instance
'''

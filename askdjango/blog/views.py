from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
    qs=Post.objects.all() #그냥 만든 것. db 접근 아직.
    q=request.GET.get('q','')
    if q:
        qs=qs.filter(title__icontains=q)
    return render(request,'blog/post_list.html',{'post_list':qs,'q':q,})


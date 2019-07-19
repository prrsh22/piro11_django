from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def post_list(request):
    qs=Post.objects.all() #그냥 만든 것. db 접근 아직.
    q=request.GET.get('q','')
    if q:
        qs=qs.filter(title__icontains=q)
    return render(request,'blog/post_list.html',{'post_list':qs,'q':q,})


def post_detail(request,id):

    post=get_object_or_404(Post,id=id) #아래 네줄보다 효율적

    '''
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404
    '''

    return render(request,'blog\post_detail.html',
                  {'post':post,})
import os
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings


# Create your views here.

def mysum(request,numbers):
    return HttpResponse(sum(list(map(lambda s:int(s or 0),numbers.split('/')))))

# lambda s: int(s or 0) --> 공백으로 입력된 부분을 0으로 바꿔줌

def hello(request,name,age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name,age))

def post_list1(requsest):
    name='공유'
    return HttpResponse('''
     <h1>AskDjango</h1>
     <p>{name}</p>
     <p>여러분의 파이썬 & 장고 페이스메이커가 되어드리겠습니다.</p>
    '''.format(name=name))

def post_list2(request):
    name='공유'
    return render(request,'dojo/post_list.html',{'name':name})


def post_list3(request):
    return JsonResponse(
        {'message':'안녕 파이썬 & 장고',
         'items':['파이썬','장고','Celery','Azure','AWS'],},
        json_dumps_params={'ensure_ascii':False}
    )

def excel_download(request):
    filepath=os.path.join(settings.BASE_DIR,'COW.xls')
    # settings.BASE_DIR: 지금 이 프로젝트가 있는 디렉토리의 절대 경로
    # --> 그 안에 엑셀 파일이 있으므로 그 경로 + 파일명 하면 경로 찾아감
    
    filename=os.path.basename(filepath)
    with open(filepath,'rb') as f:
        response=HttpResponse(f,content_type='application/vnd.ms-excel')
        response['Content-Disposition']='attatchment; filename="{}"'.format(filename)
        return response
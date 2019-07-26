from django.urls import path,re_path
from . import views,views_cbv

urlpatterns=[
    path('new/', views.post_new),
    re_path(r'^sum/(?P<numbers>[\d/]+)/$',views.mysum),
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$',views.hello),
    re_path(r'^list1/$',views.post_list1),
    re_path(r'^list2/$',views.post_list2),
    re_path(r'^list3/$',views.post_list3),
    re_path(r'^excel/$',views.excel_download),

    re_path(r'^cbv/list1/$', views_cbv.post_list1),
    re_path(r'^cbv/list2/$', views_cbv.post_list2),
    # re_path(r'^cbv/list3/$', views_cbv.post_list3),
    # re_path(r'^cbv/excel/$', views_cbv.excel_download),
 ]


from django.urls import path
from . import views,views_cbv

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('cbv/new/', views_cbv.post_new),
    path('new/',views.post_new, name='post_new'),
    path('<int:id>/edit/', views.post_edit, name='post_edit'),
]

from django.urls import path
from django.views.generic.detail import DetailView
from .views import *
from .models import Photo
# 2차 url 파일
app_name = 'photo' # name_space

urlpatterns = [
    path('', photo_list, name='photo_list'),
    # 글래스형 뷰가 아니라서 as_view가 안들어감
    path('detail/<int:pk>/', DetailView.as_view(model=Photo, template_name='photo/detail.html'),
         name='photo_detail'),
    # view.py에다 써주는게 아니라 여기다 바로 써주는 것, view에다 써줘도 짧은 내용은 그냥 써줘도됨
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    # 어떤 게시글을 delete할지 알아야하기에 int가 붙음
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]
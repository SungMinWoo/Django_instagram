from  django.urls import path

from .views import *
# 2차 url 파일
app_name = 'photo' # name_space

urlpatterns = [
    path('', photo_list, name='photo_list'),
    # 글래스형 뷰가 아니라서 as_view가 안들어감
]
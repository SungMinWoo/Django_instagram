from django.shortcuts import render

from .models import Photo
# Create your views here.

def photo_list(request):
    # 함수형 뷰는 항상 첫 번째 매개변수는 request로 넣어줌 req로 해도됨
    # 보여줄 사진 데이터
    photos = Photo.objects.all()
    # objects라는 orm 매니저한테 오브젝트 다 받아 오는 것
    return render(request, 'photo/list.html', {'photos':photos})
    # render 화면에 표시해 주는 것 request가 거의 항상 먼저 들어옴
    # 경로는 templates이 기본 경로로 깔려있음
    # object_list = photos로 바꿀 수 있음

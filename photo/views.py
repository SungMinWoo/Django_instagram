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


from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect # uploadview에서 필요함


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text'] # 작성자(author), 작성시간(created)
    template_name = 'photo/upload.html'

    def form_valid(self, form): # 입력받은 데이터가 올바르다면 저장을하는 함수
        # form 안에는 photo 모델의 인스턴스가 존재하고 입력받을 수 있는 폼을 만들어준다.
        form.instance.author_id = self.request.user.id # fk라 author라는 필드명의 id를 가져온다는 의미
        if form.is_valid():
            # 데이터가 올바르다면 저장
            form.instance.save() # 여기서 인스턴스는 model의 폼팩토리
            return redirect('/')
            # success url이 동작하는 것
        else:
            return self.render_to_response({'form':form})
            # 예를들어 회원가입할때 잘못입력하면 해당 페이지로 다시 가는데 칸이 비어있지않고 입력했던게 채워져있으려면 넣어야함


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/' # main화면
    template_name = 'photo/delete.html'


class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

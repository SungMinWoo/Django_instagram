from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
# CRUD Create, Update = 입력을 받아야하는 것은 html의 form이 필요

# 페이지 그냥 접속시 GET방식 버튼을 누르는 것은 POST
def register(request):
    if request.method == 'POST':
        # 회원 가입 데이터 입력 완료
        user_form = RegisterForm(request.POST)
        if user_form.is_valid(): # 올바르다면 데이터가 다 있다는 뜻
            new_user = user_form.save(commit=False)
            # user 폼의 세이브가 진행되면
            new_user.set_password(user_form.cleaned_data['password'])
            # 원래 폼에서 입력한 패스워드를 패스워드로 저장함
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
            # HTML로 변수를 전할 때 맨 마지막 new_user처럼 넘겨주면됨
    else:
        # 회원 가입 내용을 입력하는 상황
        user_form = RegisterForm()
    return render(request, 'registration/register.html', {'form':user_form})
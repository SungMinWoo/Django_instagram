from django.contrib.auth.models import User
from django import forms

# 폼은 html에 태그인데 프론트에서 사용자의 입력을 받는 인터페이스
# 장고의 폼 : HTML의 폼 역할, 데이터베이스에 저장할 내용을 형식, 제약조건을 결정하게됨


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput) # 비밀번호, widget의 저 값은 ***나오게하는 것
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput) # 비밀번호 확인

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        # 입력 받을 form이 자동으로 생성

    def clean_password2(self):
        cd = self.cleaned_data # sql 인잭션을 해놓은 data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']
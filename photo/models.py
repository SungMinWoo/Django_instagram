from django.db import models

# Create your models here.

# 장고의 기본 유저 모델
from django.contrib.auth.models import User
from django.urls import reverse
# models.Model에 장고의 ORM기능이 다 들어 가있어서 필드만 명시해도 기능이 동작함


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    # on_delete = 유저가 삭제할때 모든 데이터 삭제
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default="photos/no_image.png")
    # 이미지를 년월일 순으로 이미지를 저장하겠다, 기본 값이 없으면 무조건 넣어야하는 것, 예를 들어 게시글을 올리는데 사진 없이 올리는게 불가능하게 하려면 안써도됨
    text = models.TextField()
    # 텍스트필드는 기본값이 없어도 된다.
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # auto_now_add 작성한 시간, auto_now 수정한 시간을 매번 반복

    # 모델 완성 후 = makemigrations 변경사항이 뭐가 있는지 -< migrate 변경사항 저장
    class Meta:
        ordering = ['-updated']
        # 제일 최근에 찍은 사진 순으로 정렬하는 것

    def __str__(self):
        return self.author.username + "" + self.created.strftime("%Y-%m-%d %H:%M:%S")
        # 사진을 작성한 유저의 아이디값을 가져오는 것

    def get_absolute_url(self):
        # 작성이나 수정을 하면 어느 페이지로 읻오하는지
        return reverse('photo:photo_detail', args=[self.id])
from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='instagram_author_fk')
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    tag_set = models.ManyToManyField('Tag', blank=True)
    message = models.TextField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # reverse를 통한 url유지보수
    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])

    # 모델에서의 querySet
    class Meta:
        ordering = ['-id']  # id를 역순으로 정렬하겠다.


#쓰이진 않았고 admin에서 설명용으로만 작성
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='instagram_post_fk')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

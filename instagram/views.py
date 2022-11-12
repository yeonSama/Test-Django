from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from instagram.forms import PostForm
from instagram.models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs


post_list = PostListView.as_view()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅 작성완료')
        return super().form_valid(form)


post_new = PostCreateView.as_view()


class PostDetailView(DetailView):
    model = Post

    # get_queryset : 메서드를 재정의해서 사용하는 방법
    def get_queryset(self):
        qs = super().get_queryset()  # 오버로딩
        if not self.request.user.is_authenticated:  # 로그인 여부
            qs = qs.filter(is_public=True)
        return qs


# 클래스 기반 View를 사용하기위해 클래스의 as_view를 호출
post_detail = PostDetailView.as_view()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, '포스팅을 수정했습니다.')
        return super().form_valid(form)


post_edit = PostUpdateView.as_view()

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # 초기화되기전에 읽어 들어야하므로 reverse대신 reverse_lazy를 사용한다
    # reverse_lazy는 코드블럭이 수행될때 리버싱을 하지않고 사용될때에 리버싱을 해준다.
    success_url = reverse_lazy('instagram:post_list')

    # def get_success_url(self):
    #     return redirect('instagram:post_list')


post_delete = PostDeleteView.as_view()
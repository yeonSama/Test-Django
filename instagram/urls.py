from django.urls import path

from instagram import views

app_name = 'instagram'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/detail/', views.post_detail, name= 'post_detail'),#간략화 정규표현식
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
]

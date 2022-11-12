from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts import views
from accounts.forms import LoginForm

app_name = 'accounts'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('login/', LoginView.as_view(template_name='accounts/login_form.html', form_class=LoginForm, ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # login,logout은 view를 따로 안만들어주고 url에서 다 해줌
    path('signup/', views.singup, name='signup'),
]

# from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from accounts.forms import ProfileForm
from accounts.models import Profile


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


profile = ProfileView.as_view()


# 이아랫부분 해석 필요
@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, "accounts/profile_form.html", {
        'form': form
    })


User = get_user_model()


class SingupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'accounts/singup_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        auth_login(self.request, user)
        # auth_login의 참조 login as auth_login 안떠서 직접 참조함
        return response


singup = SingupView.as_view()

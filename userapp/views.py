from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm


class LoginUser(LoginView):
    authentication_form = LoginUserForm
    template_name = 'userapp/login.html'
    extra_context = {'title': 'Авторизация'}

    def login_user(request):
        if request.method == "POST":
            form = LoginUserForm(request.POST)
            if form.is_valid():
                user = authenticate(request,
                                    username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password']
                                    )
                if user and user.is_active:
                    login(request, user)
                    return redirect('profile')
        else:
            form = LoginUserForm()
        return render(request, 'userapp/profile.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('userapp:login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'userapp/profile.html'
    extra_context = {'title': "Профиль пользователя"}

    def get_success_url(self):
        return reverse_lazy('userapp:profile')

    def get_object(self, queryset=None):
        return self.request.user





class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("userapp:password_change_done")
    template_name = "userapp/password_change_form.html"
    extra_context = {'title': "Изменение пароля"}

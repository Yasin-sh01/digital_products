from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from django.urls import reverse_lazy

from .forms import RegisterForm

from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    def post(self, request):
        form = RegisterForm(request.POST)
        try:
            if form.is_valid:
                user = form.save()
                login(request, user)
                return redirect('profile')
        except:
            return HttpResponseBadRequest('error')























'''class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response'''


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
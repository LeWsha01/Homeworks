from django.shortcuts import render

# Create your views here.
from django import urls
from django.contrib.auth import views
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth import models
from authentication import forms


class LoginView(views.LoginView):
    form_class = forms.LoginForm
    template_name = 'login.html'
    success_url = urls.reverse_lazy('projects-list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/projects/')
        return super().dispatch(request, *args, **kwargs)


class LogoutView(views.LogoutView):
    next_page = urls.reverse_lazy('login')


class SignUp(generic.CreateView):
    form_class = forms.SignUpForm
    template_name = 'sign_up.html'
    success_url = urls.reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        developers = models.Group.objects.get(name='Developer')
        user.groups.add(developers)
        return redirect('/login/')
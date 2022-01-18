from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from mainapp.models import Mainapp
from django.contrib.auth.models import User

from mainapp.forms import RegisterForm, LoginForm, AddText


def logout_user(request):
    logout(request)
    return redirect('login')


def main_page(request):
    if (request.user.is_authenticated):
        name = request.user.username
        pk = request.user.pk
        text_user = Mainapp.objects.get(pk=pk)
        if request.method == "POST":
            form = AddText(request.POST)
            if form.is_valid():
                text_user.text = form.cleaned_data.get("text")
                text_user.save()
        else:
            text_dict = {
                "text":text_user
            }
            form = AddText(initial=text_dict)
        return render(request, 'mainapp/main.html',{'name':name,'form':form})
    else:
        return redirect('login')

class Register(CreateView):
    form_class = RegisterForm
    template_name = 'mainapp/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        username = form.cleaned_data.get("username")
        Mainapp.objects.create(text='', name=User.objects.get(username=username))
        return redirect('main_page')


class Login(LoginView):
    form_class = LoginForm
    template_name = 'mainapp/login.html'

    def get_success_url(self):
        return reverse_lazy('main_page')

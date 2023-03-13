from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import NewUserForm
from django.views import View

# Create your views here.

# class RegisterUser(CreateView):
#     model = User
#     form_class = UserCreationForm
#     template_name = 'accounts/create.html'
#     success_url = '/categories'

class RegisterUser(CreateView):
    model = User
    form_class = NewUserForm
    template_name = 'accounts/create.html'
    success_url = '/categories'

class ProfileView(View):
    def get(self, request):
        # return HttpResponse('--Welcome--')
        return redirect('home')
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

from todolist.forms import TaskForm
from .models import Task
# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user is not None:
                login(request, user)  # melakukan login terlebih dahulu
                response = HttpResponseRedirect(
                    reverse("todolist:show_todolist"))  # membuat response
                # membuat cookie last_login dan menambahkannya ke dalam response
                response.set_cookie('last_login', str(datetime.datetime.now()))
                response.set_cookie('username', username)
                return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.all()
    context = {
        'list_task': data_task,
        'username': request.COOKIES['username'],
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def add_task(request):

    if request.method == "POST":
        form = TaskForm(request.POST)
        try:
            form.save()
            print('Berhasil nyimpan')
        except ValueError as e:
            print(e)
    
    context = {'form': TaskForm()}
    return render(request, 'add_task.html', context)
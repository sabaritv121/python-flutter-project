from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views
from django.views.decorators.csrf import csrf_exempt

from work_app.forms import Userregister
from work_app.models import Login


def home(request):
    return render(request,'index.html')


def userlist(request):
    data = Login.objects.filter(is_user=1)
    return render(request,'user-view.html',{'data':data})

def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user = authenticate(request, username=name, password=pwd)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('adminhome')

        else:
            messages.info(request, "invalid credentials")

    return render(request,'login.html')


def adhome(request):
    return render(request,'subadminhome.html')


def view_workshop(request):
    work = Login.objects.filter(is_workshop=True)
    return render(request, 'viewwork.html', {'work': work})

def view_customer(request):
    work = Login.objects.filter(is_user=True)
    return render(request, 'vieww.html', {'work': work})
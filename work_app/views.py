from django.http import JsonResponse
from django.shortcuts import render

# Create your views
from django.views.decorators.csrf import csrf_exempt

from work_app.forms import Userregister
from work_app.models import Login


def home(request):
    return render(request,'index.html')


def userlist(request):
    data = Login.objects.filter(is_user=1)
    return render(request,'user-view.html',{'data':data})


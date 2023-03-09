from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from work_app.forms import Userregister, MechanicRegister
from work_app.models import Workrequest, Login, Youtube_link
from work_app.serializers import WrequestSerializer, WorkSerializer, ReviewSerializer, YoutubeSerializer


@csrf_exempt
def user_registration(request):
    result_data=None
    if request.method=='POST':
        form=Userregister(request.POST)
        # fullname=request.POST.get('full name')
        # uname=fullname+str(random.randint(0,999))
        if form.is_valid():
            form=form.save(commit=False)
            form.is_active=True
            form.is_user=True
            form.save()
            result_data=True
    try:
        if result_data:
            data={'result':True}
        else:
            print(list(form.errors))
            error_data=form.errors
            error_dict={}
            for i in list(form.errors):
                error_dict[i]=error_data[i][0]
                data={
                    'result':False,
                    'errors':error_dict
                }
    except:
        data={
            'result':False
        }
    return JsonResponse(data,safe=False)



@csrf_exempt
def Mechanic_registration(request):
    result_data=None
    if request.method=='POST':
        form=MechanicRegister(request.POST)
        # fullname=request.POST.get('full name')
        # uname=fullname+str(random.randint(0,999))
        if form.is_valid():
            form=form.save(commit=False)
            form.is_active=True
            form.is_workshop=True
            form.save()
            result_data=True

    try:
        if result_data:
            data={'result':True}
        else:
            print(list(form.errors))
            error_data=form.errors
            error_dict={}
            for i in list(form.errors):
                error_dict[i]=error_data[i][0]
                data={
                    'result':False,
                    'errors':error_dict
                }
    except:
        data={
            'result':False

        }
    return JsonResponse(data,safe=False)



@csrf_exempt
def login_views(request):
    print('hiii')
    if request.method == 'POST':
        print('hiiiIII')
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            print('hii87')
            login(request,user)
            print(user)
            if user.is_user:
                type = 'user'
                print('hii8')
            elif user.is_workshop:
                print("test")
                type = 'workshop'
                # result = user.is_authenticated
                print('hii8')
    try:
        result = user.is_authenticated

        data = {
            'status':True,
            'result':{
                'id':user.id,
                'name':user.username,
                'type':type
            }
        }
    except:
        data = {
            'result':False
        }
    return JsonResponse(data, safe=False)



#work request

@api_view(['GET','POST'])
def Wrequest_view(request):
    if request.method =='GET':
        req = Workrequest.objects.all()
        serializer=WrequestSerializer(req,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WrequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def workshopview(request):
    if request.method =='GET':
        work = Login.objects.filter(is_user=0)
        serializer=WorkSerializer(work,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def workshopview(request):
    if request.method =='GET':
        work = Login.objects.filter(is_user=0)
        serializer=WorkSerializer(work,many=True)
        return Response(serializer.data)


@api_view(['GET','POST'])
def Review(request):
    if request.method == "POST":
        print("helo")
        data1= ReviewSerializer(data=request.data)
        print(data1)
        if data1.is_valid():
            print("hello")
            data1.save()
            return Response(data1.data, status=status.HTTP_201_CREATED)
        return Response(data1.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST'])
def Ytlink(request):
    if request.method =='GET':
        req = Youtube_link.objects.all()
        serializer=YoutubeSerializer(req,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = YoutubeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
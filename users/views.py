from django.shortcuts import render
from .models import users
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import UserForm
from django.contrib import messages
from rest_framework import viewsets
from .models import ToDo 
from .serializers import ToDoSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
def show_users(request):
    all_users=users.objects.all()
    data={
        "users": all_users
    }
    return render(request,"students.html",data)

def add_user(request):
    if request.method == "POST":
        name=request.POST.get("name")
        age=request.POST.get("age")

        users.objects.create(
            name=name,
            age=age
        )
    return render(request,"add_users.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        User.objects.create_user(
            username=username,
            password=password
        )

    return render(request,"signup.html")

def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(
            request,
            username=username,
            password=password
        )   
        if user is not None:

            login(request, user)
            messages.success(request,"user logined succesfully")

    return render(request,"login.html")

def logout_user(request):
    logout(request)

    return HttpResponse("Logged Out")

def form_page(request):

    form = UserForm()

    return render(request,
                  "forms.html",
                  {"form": form})


class ToDoViewSet(viewsets.ModelViewSet):

    queryset = ToDo.objects.all()

    serializer_class = ToDoSerializer

    filter_backends=[SearchFilter,DjangoFilterBackend]

    search_fields=  ['task']

    filterset_fields=['completed']
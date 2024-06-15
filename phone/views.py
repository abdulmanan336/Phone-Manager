from django.shortcuts import render,redirect
from . import models
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def signout(request):
    logout(request)
    return redirect('user')


def user(request):
    return render(request,'user.html')


def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        try:
            user = User.objects.create_user(username=username,email=email,password=password)
            login(request,user)
            return redirect('main')
        except IntegrityError:
            return render(request , 'user.html', {'error_message': 'Username doesnot exsit '})

def main(request):
    if request.user.is_authenticated:
        contact = models.contact.objects.filter(user=request.user)
        context = {'contact': contact}
        return render(request,'main.html',context)
    else:
        return render(request,'user.html')

def add(request):
    category = models.Category.objects.all()
    return render(request,'add.html', {'category':category})
def form(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        adress = request.POST.get('adress')
        postaladress = request.POST.get('postaladress')
        city = request.POST.get('city')
        user = request.user
    models.contact.objects.create(first_name=first_name,user=user,last_name=last_name,email=email,phone=phone,adress=adress,postaladress=postaladress,city=city)
    return redirect('main')


def del_contact(request, id):
    
    contact = models.contact.objects.get(id=id)
    contact.delete()
    return JsonResponse({"result":"deleted"})

def view(request, id):
    contact = models.contact.objects.get(id=id)
    context = {'contact':contact}
    return render(request,'view.html',context)


def search(request):
    q = request.GET.get('q')
    if q is not None:
        contact = models.contact.objects.filter(first_name__contains=q)
    else:    
        contact = models.contact.objects.all()
    context = {'contact': contact}
    return render(request,'search.html',context)

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)
        if user:
            login(request, user)
            return redirect('main')
        else:
            return render(request,'user.html', {'error_message': 'Invalid username or password '}) 




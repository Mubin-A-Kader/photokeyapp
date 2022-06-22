from django.shortcuts import render, redirect
from .models import Category, Photo,Photo2
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')

    return render(request, 'photos/login_register.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('gallery')

    context = {'form': form, 'page': page}
    return render(request, 'photos/login_register.html', context)


@login_required(login_url='login')
def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photos2 = Photo.objects.filter(category__user=user,image__endswith=".jpg")
        photos = Photo.objects.filter(category__user=user,image__endswith=".mp4")
    else:
        photos = Photo.objects.filter(
            category__name=category, category__user=user,image__endswith=".mp4")
        photos2 = Photo.objects.filter(
            category__name=category, category__user=user,image__endswith=".jpg")     
        
        
    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'photos': photos,'photos2': photos2}
    return render(request, 'photos/gallery.html', context)


@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    
    
    
    return render(request, 'photos/key.html')
    
        #return render(request, 'photos/photo.html', {'photo': photo})
@login_required(login_url='login')
def zlewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    
    return render(request, 'photos/photo.html', {'photo': photo})    
        

debuggg = 0

    


@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        formail = request.POST['email']
        formkey = request.POST['key']
      
        myuser = Photo.objects.create(eemail=formail,key=formkey)
   
        subject = "Welcome to Our website!"
        message =  "Your key is " +" "+  myuser.key   
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.eemail]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                key=data['key'],
                eemail=data['email'],
                image=image,
                
            )
        
        
   

       
        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)


@login_required(login_url='login')
def addVideo(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image2 in images:
            photo2 = Photo2.objects.create(
                category=category,
                description=data['description'],
                image2=image2,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context)

import os
@login_required(login_url='login')    
def keyVerify(request):
    
    
    
    if request.method == 'POST':
        formkey = request.POST['key']
        print(formkey)
        myuser = Photo.objects.all()
        for i in myuser:
            
            x = i.key
        
        if x == formkey:
            photo = Photo.objects.filter(key__startswith=x)
            
            
        
       
      
    
            
            
            
            
            
            return render(request, 'photos/photo.html',{"photo":photo})
        else:
            return redirect("/")
        #photo = Photo.objects.filter(id=idee)
        
        #return render(request, 'photos/photo.html', {'photo': photo})
        #else:
@login_required(login_url='login')    
def keyhtml(request):
    return render(request,"photos/key.html")
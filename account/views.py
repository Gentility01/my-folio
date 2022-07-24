from django.shortcuts import render, redirect
# from django.contrib.auth.forms import  UserCreationForm
from django.contrib import messages
from .forms import CreateUserForms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required


# Create your views here.



def register_view(request):
    if request.user.is_authenticated:
        return redirect('blog_view')
    else:
        form = CreateUserForms()
        if request.method == 'POST':
            form = CreateUserForms(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Message sent successfully")
                return HttpResponseRedirect('login')
        
        context = {
            'form':form
        }
        return render(request, 'account/register.html', context)

def login_view(request):
    if request.user.is_authenticated:
         return redirect('blog_view')
    else:
        if request.method == 'POST':
            username =  request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('blog_view')
            else:
                messages.info(request,"Message sent successfully")
                return HttpResponseRedirect('login')
        return render(request,  'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from site_pages.models import SiteModels
from .forms import SiteForm,SignupForm,EditProfileForm,ProfileImageForm
from django.db import models
from django.db.models import Count
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User

# Create your views here.
def signuppage(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Your account has been created")
            return redirect("loginpage")
    else:
        form = SignupForm()

    return render(request, "site_pages/signup.html", {"form": form})


def loginpage(request):
    if request.method=="POST": 
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get("password")
            user=authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('homepage')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form=AuthenticationForm()
    return render(request, 'site_pages/login.html', {"form":form})

def logoutpage(request):
    logout(request)
    return redirect("loginpage")

@login_required(login_url='loginpage')
def profilepage(request):
    return render(request, 'site_pages/profile.html')

@login_required(login_url='loginpage')
def editprofile(request):
    user = request.user
    profile = user.userprofile

    if request.method == "POST":
        user_form = EditProfileForm(request.POST, instance=user)
        profile_form = ProfileImageForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():

            # If user checked "remove photo"
            if profile_form.cleaned_data.get("remove_photo"):
                if profile.image and profile.image.name != "profile_pics/default.png":
                    profile.image.delete(save=False)
                profile.image = "profile_pics/default.png"

            user_form.save()
            profile_form.save()

            messages.success(request, "Profile updated.")
            return redirect("profilepage")

    else:
        user_form = EditProfileForm(instance=user)
        profile_form = ProfileImageForm(instance=profile)

    return render(request, "site_pages/editprofile.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })


@login_required(login_url='loginpage')  
def homepage(request):
    return render(request, "site_pages/home.html")

@login_required(login_url='loginpage')
def aboutpage(request):
    return render(request, "site_pages/about.html")

@login_required(login_url='loginpage')
def contactpage(request):
    return render(request, "site_pages/contact.html")

@login_required(login_url='loginpage')
def addform(request):
    if request.method=="POST":
        form=SiteForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.author=request.user
            task.save()
            messages.success(request, 'Task was added successfully!')
            return redirect ('formpage')
    else:
        form=SiteForm()

    query=request.GET.get('q')
    tasks=SiteModels.objects.filter(author=request.user)
    if query:
        tasks=tasks.filter(
            models.Q(title__icontains=query) |
            models.Q(description__icontains=query)
        )

    tasks=tasks.order_by("-created_at")
    paginator=Paginator(tasks,5)    #5 task per page
    page_number= request.GET.get("page")
    page_obj=paginator.get_page(page_number)
    return render(request, 'site_pages/form.html', {
        'form': form ,
        'tasks':page_obj,
        "page_obj":page_obj
        })

@login_required(login_url='loginpage')
def deletetask(request, id):
    task=SiteModels.objects.get(id=id, author=request.user)
    task.delete()
    messages.success(request, 'Task was deleted successfully!')
    return redirect('formpage')

@login_required(login_url='loginpage')
def updatetask(request, id):
    task=SiteModels.objects.get(id=id, author=request.user)
    if request.method=="POST":
        form=SiteForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task was updated successfully!')
            return redirect ('formpage')
    else:
        form=SiteForm(instance=task)
    return render(request, 'site_pages/formupdate.html', {'form': form})


@login_required(login_url='loginpage')
def deleteprofile(request):
    if request.method=='POST':
        request.user.delete()
        messages.success(request,"Account Successfully Deleted!")
        return redirect('signuppage')
    return render(request, 'site_pages/deleteprofile.html')

@login_required(login_url='loginpage')
def completetask(request, id):
    task = SiteModels.objects.get(id=id, author=request.user)
    task.is_completed = True
    task.save()
    return redirect('formpage') 

@login_required(login_url='loginpage')
def staffdashboard(request):
    if not request.user.is_staff:
        return HttpResponseForbidden('you are not authorized to view this page')
    return render(request, 'site_pages/staffdashboard.html')


@login_required(login_url='loginpage')
def dashboardstatus(request):
    if not request.user.is_staff:
        return HttpResponseForbidden('You have no access to view this page')   
    
    users=User.objects.annotate(task_count=Count("sitemodels")).order_by('-task_count')
    total_users=User.objects.count()
    total_tasks=SiteModels.objects.count()
    return render(request, 'site_pages/dashboard.html', {
        'user':users,
        'total_users':total_users,
        'total_tasks':total_tasks,
    })
    
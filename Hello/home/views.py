from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import submit
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    context = {
        "variable1":"Harry is great",
        "variable2":"Rohan is great"
    } 
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')
 

def addbook(request):
    if request.method == "POST":
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        # phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = submit(name=name, quantity=quantity, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your book is added!')
    return render(request, 'addbook.html')
 
def inventory(request):
    list = submit.objects.all()
    return render (request, 'inventory.html',
    {'list': list})

def delete(request):
    if request.method == "POST":
        name = request.POST.get('name')
        # quantity = request.POST.get('quantity')
        # # phone = request.POST.get('phone')
        # desc = request.POST.get('desc')
        contact = submit(name=name)
        contact.delete()
        messages.success(request, 'Your book deleted!')
    return render(request, 'delete.html')
        

def update(request):
    if request.method == "POST":
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        # quantity = request.POST.get('quantity')
        # # phone = request.POST.get('phone')
        # desc = request.POST.get('desc')
        contact = submit(name=name, quantity=quantity, date = datetime.today())
        contact.save()
        messages.success(request, 'Your update was made!')
    return render(request, 'update.html')


def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        email =  request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username,email,password)
        myuser.name = username
        myuser.save()
        return redirect('home')
    else:
        return HttpResponce('404 -not found')    


def handlelogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user = authenticate(username= loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


   
    
    



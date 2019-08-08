from django.shortcuts import render, redirect
from django.contrib import auth 
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    # if POST 
    if request.method == 'POST':
        #get form info
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #check passwords match
        if password == password2:
            #check if a user exists with username
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Username is already taken.'})
            #check if a user exists with email 
            else: 
                if User.objects.filter(email=email).exists():
                    return render(request, 'register.html', {'error': 'That email already exists. Please log in.'})
                else: 
                    #if everything is ok Create a User
                    user = User.objects.create_user(
                        username=username, password=password,
                        email=email, first_name=first_name,
                        last_name=last_name
                    )
                    user.save()
                    return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    # else
    else:
        #send form
        return render(request, 'register.html')

def login(request):
    # if POST
    if request.method == 'POST':
        #GET form info
        username = request.POST['username']
        password = request.POST['password']
        # authenricate user
        user = auth.authenticate(username=username, password=password)
        #make suer a user exists
        if user is not None:
            #login
            auth.login(request, user)
            #redirect
            return redirect('profile')
        # else return not found
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    else: 
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('artist_list')
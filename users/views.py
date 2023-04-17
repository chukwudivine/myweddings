from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        try:
            user = User.objects.create_user(request.POST['username'], email=request.POST['email'], password=request.POST['password'])
            user.save()
            login(request, user)
            return redirect('home')
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'Username already taken. Choose new username.'})

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'This user does not exist!'})


@login_required
def log_out(request):
    logout(request)
    return redirect('home')



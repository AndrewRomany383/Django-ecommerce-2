from django.shortcuts import render, redirect
from .forms import RegisterationForm
from .models import Account
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.




def register(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = email.split('@')[0]
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,username=username , password=password, phone_number=phone_number)
            user.save()
            return redirect('home:home')
    else:
        form = RegisterationForm()
    context = {
        'form':form
    }
    return render(request, 'Accounts/register.html', context)



def log_in(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')

        else:
            messages.error(request, 'invalid login details')
            return redirect('Accounts:login')

    return render(request, 'Accounts/login.html')

























































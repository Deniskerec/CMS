from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Records


def home(request):
    records = Records.objects.all()

    if request.method == 'POST':
        #From the home.html form, we will sign the values to username and to password variable.
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.success(request, 'Invalid Credentials')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registered')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register_user.html', {'form': form})
    return render(request, 'register_user.html', {'form': form})


def monthly_record(request, pk):
    if request.user.is_authenticated:
        # Look up record
        monthly_record = Records.objects.get(id=pk)
        return render(request, 'monthly_record.html', {'monthly_record': monthly_record})
    else:
        messages.success(request, 'Login')

        return redirect('home')


def delete_monthly_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Records.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record deleted')
        return redirect('home')
    else:
        messages.success(request, 'Not logged in')
        return redirect('home')


def add_monthly_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        return render(request, 'add_monthly_record.html', {'form': form})
    else:
        messages.success(request, "Log In - cmon")
        return redirect('home')


def update_monthly_record(request, pk):
    if request.user.is_authenticated:
        current_month = Records.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_month)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated")
            return redirect('home')
        return render(request, 'update_monthly_record.html', {'form': form})
    else:
        messages.success(request, "Log In - cmon not logged in")

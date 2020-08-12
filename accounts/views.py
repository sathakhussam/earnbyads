from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import forms

def signup_acc(request):
    form = forms.SignupForm()
    context = {'form':form}
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        print('here')
        if form.is_valid():
            form.clean_password2()
            # form.save()
            return redirect('dashboard')
            print('saved')
    return render(request, 'accounts/signup.html',context)

def login_acc(request):
    form = forms.LoginForm
    context = {'form':form}
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            if form.login_acc(request):
                return redirect('dashboard')
            else:
                context['error'] = "The user and password doesn't match."
    return render(request, 'accounts/login.html',context)

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


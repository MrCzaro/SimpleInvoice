from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import CustomAuthenticationForm, CustomUserCreationForm

def signup_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else: 
        form = CustomUserCreationForm()
    
    context = {
        "form" : form,
        "title" : "Signup"
    }
    
    return render(request, "accounts.html", context)            
        

def login_user(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            email=form.cleaned_data.get("email")
            password=form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("invoice:dashboard")
            else:
                messages.error(request, "Invalid login credentials. Please try again.")
    else: 
        form = CustomAuthenticationForm(request)
    
    context = {
        "form" : form,
        "title" : "Login",
    }
    
    return render(request, "accounts.html", context)
        
def logout_user(request):
    logout(request)
    return redirect("accounts:login")
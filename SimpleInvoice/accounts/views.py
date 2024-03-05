from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else: 
        form = CustomUserCreationForm()
    
    context = {
        "form" : form,
        "title" : "Registration"
    }
    
    return render(request, "signup.html", context)            
        

def login(request):
    pass

def logout(request):
    pass
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return render(request, 'index.html')  
    
    
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        pass
    


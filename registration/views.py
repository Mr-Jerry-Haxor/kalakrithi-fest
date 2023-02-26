from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import qrcontent

def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return render(request, 'index.html')  
    
@csrf_exempt  
def register(request):
    if request.method == 'GET':
      data = {'registrar': request.user.first_name}
      form = qrcontent(data)
      return render(request,'register.html', {'form':form})
    elif request.method == 'POST':
        qrcode = request.POST.get('qrtext')
        print(qrcode)
        print(request.POST.get)
        return render(request,'register.html')
    


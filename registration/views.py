from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import qrcontent , student_details
from .models import qrvalues , participant ,registrar

def home(request):
    if request.user.is_authenticated:
      if registrar.objects.filter(email=request.user.email).exists():
        return render(request,'home.html')
      else:
        return redirect("logout")
    else:
        return render(request, 'index.html')  
    
def savedetails(request): 
  if request.user.is_authenticated:
    if request.method == 'POST':
      fullname = request.POST.get('fullname')
      registrationnumber = request.POST.get('registrationnumber')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      year = request.POST.get('year')
      branch = request.POST.get('branch')
      institute = request.POST.get('institute')
      campus = request.POST.get('campus')
      qrtext = request.POST.get('qrtext')
      qrhash = request.POST.get('qrhash')
      registrar = request.POST.get('registrar')
      if participant.objects.filter(registrationnumber=registrationnumber).exists():
        return render(request, 'message.html', {'message':'The student is already got registred'})
      elif participant.objects.filter(qrtext = qrtext).exists():
        return render(request, 'message.html', {'message':'The PASS QR is already got registred'})
      else:
        details = participant(fullname=fullname,registrationnumber=registrationnumber,email=email,phone=phone,year=year,branch=branch,institute=institute,campus=campus,qrtext=qrtext,qrhash=qrhash,registrar=registrar)
        details.save()
        status = "Your details updated successfully"
        return redirect("/register",{'error': status})
  else:
    return render(request, 'index.html')
     


def register(request):
  if request.user.is_authenticated:
    if request.method == 'GET':
      data = {'registrar': request.user.first_name}
      form = qrcontent(data)
      return render(request,'register.html', {'form':form})
    elif request.method == 'POST':
      qrcode = request.POST.get('qrtext')
      qrdataset = qrvalues.objects.filter(qrhash=qrcode).values()
      print(qrdataset)
      qrtext = qrdataset[0]['qrtext']
      qrhash = qrdataset[0]['qrhash']
      sdata = {'qrtext':qrtext, 'qrhash':qrhash,'registrar': request.user.first_name}
      studentform = student_details(sdata)
      if participant.objects.filter(qrtext = qrtext).exists():
        return render(request, 'message.html', {'message':'The PASS QR is already got registred'})
      else:
        return render(request, 'student_details.html',{'form':studentform})
  else:
    return render(request, 'index.html') 
      
      
        
    


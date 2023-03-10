from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import qrcontent, student_details, verify_details, outentryupdateform
from .models import qrvalues, participant, registrar, verification_status, entries
from django.contrib import messages

from datetime import datetime
from datetime import timedelta
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings


def home(request):
  if request.user.is_authenticated:
    if registrar.objects.filter(email=request.user.email).exists():
      return render(request, 'home.html')
    else:
      return redirect("logout")
  else:
    return render(request, 'index.html')


def send_confirmation_mail(fullname, registrationnumber, email, qrhash):
  subject, from_email, to = 'Kalakrithi Fest pass confirmation', settings.EMAIL_HOST_USER, email
  html_content1 = get_template('confirmation.html').render({'name':fullname, 'regno': registrationnumber})
  msg = EmailMultiAlternatives(subject, html_content1, from_email, [to])
  msg.content_subtype = "html"
  msg.send()


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
      if participant.objects.filter(
          registrationnumber=registrationnumber).exists():
        return render(request, 'message.html',
                      {'message': 'The student is already got registred'})
      elif participant.objects.filter(qrtext=qrtext).exists():
        return render(request, 'message.html',
                      {'message': 'The PASS QR is already got registred'})
      else:
        details = participant(fullname=fullname,
                              registrationnumber=registrationnumber,
                              email=email,
                              phone=phone,
                              year=year,
                              branch=branch,
                              institute=institute,
                              campus=campus,
                              qrtext=qrtext,
                              qrhash=qrhash,
                              registrar=registrar)
        details.save()
        #send_confirmation_mail(fullname, registrationnumber, email, qrhash)
        messages.success(request, 'Participant details updated.')
        return redirect("/register")
    else:
      return redirect('home')
  else:
    return redirect('home')


def register(request):
  if request.user.is_authenticated:
    if request.method == 'GET':
      data = {'registrar': request.user.first_name}
      form = qrcontent(data)
      passessold = len(participant.objects.all())
      return render(request, 'register.html', {
        'form': form,
        'passessold': passessold
      })
    elif request.method == 'POST':
      qrcode = request.POST.get('qrtext')
      if qrvalues.objects.filter(qrhash=qrcode).exists():
        qrdataset = qrvalues.objects.filter(qrhash=qrcode).values()
        qrtext = qrdataset[0]['qrtext']
        qrhash = qrdataset[0]['qrhash']
        sdata = {
          'qrtext': qrtext,
          'qrhash': qrhash,
          'registrar': request.user.first_name
        }
        studentform = student_details(sdata)
        if participant.objects.filter(qrtext=qrtext).exists():
          return render(request, 'message.html',
                        {'message': 'The PASS QR is already got registred'})
        else:
          return render(request, 'student_details.html', {'form': studentform})
      else:
        return render(request, 'message.html', {'message': 'Invalid QR'})
  else:
    return redirect('home')


def verify(request):
  if request.user.is_authenticated:
    if request.method == "GET":
      data = {'registrar': request.user.first_name}
      form = qrcontent(data)
      admitted = len(verification_status.objects.filter(status="IN"))
      out = len(verification_status.objects.filter(status="OUT"))
      return render(request, 'verify.html', {
        'form': form,
        'admitted': admitted,
        'out': out
      })
    else:
      qrcode = request.POST.get('qrtext')
      if participant.objects.filter(qrhash=qrcode).exists():
        entry = participant.objects.filter(qrhash=qrcode).values()
        if verification_status.objects.filter(qrhash=qrcode).exists():
          if verification_status.objects.filter(
              Q(qrhash=qrcode) & Q(status="OUT")).exists():
            vdata = {
              'fullname': entry[0]['fullname'],
              'registrationnumber': entry[0]['registrationnumber'],
              'email': entry[0]['email'],
              'phone': entry[0]['phone'],
              'year': entry[0]['year'],
              'branch': entry[0]['branch'],
              'institute': entry[0]['institute'],
              'campus': entry[0]['campus'],
              'qrtext': entry[0]['qrtext'],
              'qrhash': entry[0]['qrhash'],
              'verifiedby': request.user.first_name
            }
            vform = verify_details(vdata)
            imglink = f"https://doeresults.gitam.edu/photo/img.aspx?id={entry[0]['registrationnumber']}"
            if entries.objects.filter(qrhash=entry[0]['qrhash']).exists():
              entries_data = entries.objects.filter(qrhash=qrcode).values()
              return render(request, 'verify_details.html', {
                'form': vform,
                'entrydata': entries_data,
                'imglink': imglink
              })
            else:
              return render(request, 'verify_details.html', {
                'form': vform,
                'imglink': imglink
              })
          elif verification_status.objects.filter(
              Q(qrhash=qrcode) & Q(status="IN")).exists():
            entries_data = entries.objects.filter(qrhash=qrcode).values()
            sdata = {
              'qrhash': qrcode,
            }
            imglink = f"https://doeresults.gitam.edu/photo/img.aspx?id={entry[0]['registrationnumber']}"
            return render(
              request, 'admitted.html', {
                'entrydata': entries_data,
                'qrhash': qrcode,
                'registrationnumber': entry[0]['registrationnumber'],
                'imglink' : imglink,
                'form': outentryupdateform(sdata)
              })
        else:
          qrcode = request.POST.get('qrtext')

          vdata = {
            'fullname': entry[0]['fullname'],
            'registrationnumber': entry[0]['registrationnumber'],
            'email': entry[0]['email'],
            'phone': entry[0]['phone'],
            'year': entry[0]['year'],
            'branch': entry[0]['branch'],
            'institute': entry[0]['institute'],
            'qrtext': entry[0]['qrtext'],
            'qrhash': entry[0]['qrhash'],
            'verifiedby': request.user.first_name
          }
          vform = verify_details(vdata)
          imglink = f"https://doeresults.gitam.edu/photo/img.aspx?id={entry[0]['registrationnumber']}"
          return render(request, 'verify_details.html', {
            'form': vform,
            'imglink': imglink
          })
      else:
        messages.success(request, 'Invalid QR')
        return redirect('verify')     #render(request, 'message.html', {'message': 'Invalid QR'})
  else:
    return redirect('home')


def verifydetails(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      if verification_status.objects.filter(
          Q(qrhash=request.POST.get('qrhash')) & Q(status="OUT")).exists():
        verification_status.objects.filter(
          qrhash=request.POST.get('qrhash')).update(status='IN')
        utc = datetime.now()
        ist = utc + timedelta(hours=5, minutes=30)
        todaydate = datetime.date(ist)
        timenow = datetime.time(ist)
        entry_update = entries(
          registrationnumber=request.POST.get('registrationnumber'),
          qrtext=request.POST.get('qrtext'),
          qrhash=request.POST.get('qrhash'),
          date=todaydate,
          time=timenow,
          verifiedby=request.POST.get('verifiedby'),
          status="IN")
        entry_update.save()
        return redirect('verify')
      else:

        fullname = request.POST.get('fullname')
        registrationnumber = request.POST.get('registrationnumber')
        email = request.POST.get('email')
        qrtext = request.POST.get('qrtext')
        qrhash = request.POST.get('qrhash')
        verifiedby = request.POST.get('verifiedby')
        status = "IN"
        status_update = verification_status(
          fullname=fullname,
          registrationnumber=registrationnumber,
          email=email,
          qrtext=qrtext,
          qrhash=qrhash,
          status=status)
        status_update.save()

        utc = datetime.now()
        ist = utc + timedelta(hours=5, minutes=30)
        todaydate = datetime.date(ist)
        timenow = datetime.time(ist)
        entry_update = entries(registrationnumber=registrationnumber,
                               qrtext=qrtext,
                               qrhash=qrhash,
                               date=todaydate,
                               time=timenow,
                               verifiedby=verifiedby,
                               status="IN")
        entry_update.save()
        return redirect('verify')
    else:
      return redirect('home')
  else:
    return redirect('home')


def page_not_found_view(request, exception):
  return render(request, '404.html', status=404)


def outentryupdate(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      qrcode = request.POST.get('qrhash')

      entry = participant.objects.filter(qrhash=qrcode).values()
      verification_status.objects.filter(qrhash=qrcode).update(status='OUT')
      utc = datetime.now()
      ist = utc + timedelta(hours=5, minutes=30)
      todaydate = datetime.date(ist)
      timenow = datetime.time(ist)
      entry_update = entries(registrationnumber=entry[0]['registrationnumber'],
                             qrtext=entry[0]['qrtext'],
                             qrhash=qrcode,
                             date=todaydate,
                             time=timenow,
                             verifiedby=request.user.first_name,
                             status="OUT")
      entry_update.save()
      return redirect('verify')
    else:
      return redirect('verify')
  else:
    return redirect('home')

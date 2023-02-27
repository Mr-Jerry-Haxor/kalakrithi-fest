from django import forms

class qrcontent(forms.Form):
  qrtext = forms.CharField(max_length=300,required=True,label="Qr text" ,widget=forms.TextInput(attrs={'readonly':'readonly'}))
  registrar = forms.CharField(max_length=300,required=True, label="Registration By:",widget=forms.TextInput(attrs={'readonly':'readonly'}))


class student_details(forms.Form):
    fullname = forms.CharField(max_length=200,required=True,label="Enter your full name")
    registrationnumber = forms.CharField(max_length=100, required=True, label="Enter the Gitam registration number")
    email = forms.EmailField(max_length=200,required=True, label="Enter gitam mailid",initial="")
    phone = forms.CharField(max_length=100,required=True,label="Enter your mobile number")
    year = forms.CharField(max_length=100,required=True, label="Enter which year are you studying")
    branch = forms.CharField(max_length=100,required=True,label="Enter the branch")
    institute = forms.CharField(max_length=100,required=True,label="Enter the institute(eg: GIT, GIS)")
    campus = forms.CharField(max_length=100,required=True,label="campus")
    qrtext = forms.CharField(max_length=100,required=True,label="QR code",widget=forms.TextInput(attrs={'readonly':'readonly'}))
    qrhash = forms.CharField(max_length=100,required=True,label="QR Hash",widget=forms.TextInput(attrs={'readonly':'readonly'}))
    registrar=forms.CharField(max_length=100,required=False,label="Registrar",widget=forms.TextInput(attrs={'readonly':'readonly'}))



class verify_details(forms.Form):
  fullname = forms.CharField(max_length=200,required=True,label="Full name : ",widget=forms.TextInput(attrs={'readonly':'readonly'}))
  registrationnumber = forms.CharField(max_length=100, required=True, label="Gitam Reg no : ",widget=forms.TextInput(attrs={'readonly':'readonly'}))
  email = forms.EmailField(max_length=200,required=True, label="Gitam mailid : ",widget=forms.TextInput(attrs={'readonly':'readonly'}))
  phone = forms.CharField(max_length=100,required=True,label="Mobile number : ",widget=forms.TextInput(attrs={'readonly':'readonly'}))
  year = forms.CharField(max_length=100,required=True, label="Year : ",widget=forms.TextInput(attrs={'readonly':'readonly'}))
  branch = forms.CharField(max_length=100,required=True,label="Branch : ",widget=forms.TextInput(attrs={'readonly':'readonly'}))
  institute = forms.CharField(max_length=100,required=True,label="Institute : ",widget=forms.TextInput(attrs={'readonly':'readonly'}))
  campus = forms.CharField(max_length=100,required=True,label="Campus : ",widget=forms.TextInput(attrs={'readonly':'readonly'}))
  qrtext = forms.CharField(max_length=100,required=True,label="QR code : ",widget=forms.TextInput(attrs={'readonly':'readonly'}))
  qrhash = forms.CharField(max_length=100,required=True,label="QR Hash : ",widget=forms.TextInput(attrs={'readonly':'readonly'}))
  verifiedby =forms.CharField(max_length=100,required=False,label="Verified By : ",widget=forms.TextInput(attrs={'readonly':'readonly'}))

class outentryupdateform(forms.Form):
  qrhash = forms.CharField(max_length=100,required=True,label="QR Hash : ",widget=forms.TextInput(attrs={'readonly':'readonly'}))
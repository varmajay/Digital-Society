from dataclasses import dataclass
from random import randrange
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail

from myapp.models import Secretary

# Create your views here.

def index(request):
    return render(request,'index.html')


def login(request):
    try:
        uid=Secretary.objects.get(email=request.session['email'])
        return redirect('index')
    except:
        if request.method == 'POST':
            try:
                uid = Secretary.objects.get(email=request.POST['email'])
                if request.POST['password'] == uid.password:
                    request.session['email'] = request.POST['email']
                    return redirect('index')
                return render(request,'login.html',{'msg':'Please Enter Valid Password'})
            except:
                msg='Your Email Is Not Register '
                return render(request,'login.html',{'msg':msg})
    return render(request,'login.html')



def logout(request):
    del request.session['email']
    return redirect('login')




def register(request):
    if request.method == 'POST':
        try:
            Secretary.objects.get(email=request.POST['email'])
            msg='Email is Already Register'
            return render(request,'register.html',{'msg':msg})
        except:
            if len(request.POST['password'])>7:
                if request.POST['password'] == request.POST['cpassword']:
                    otp=randrange(1000,9999)
                    subject = 'welcome to Digital Society'
                    message = f"""Hello {request.POST['name']},
                    Your OTP is {otp}"""
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [request.POST['email'], ]
                    send_mail( subject, message, email_from, recipient_list )
                    global data
                    data={
                        "name":request.POST['name'],
                        "email":request.POST['email'],
                        "phone":request.POST['phone'],
                        "address":request.POST['address'],
                        "password":request.POST['password'],
                        "pic":request.POST['pic'],
                    }
                    return render(request,'otp.html',{'otp':otp})
                return render(request,'register.html',{'msg':'Password must be same'})
            return render(request,'register.html',{'msg':'Password must be Atleast 8 Character'})
    return render(request,'register.html')

def otp(request):
    if request.method == 'POST':
        if request.POST['otp'] == request.POST['cotp']:
            global data
            Secretary.objects.create(
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                address=data['address'],
                password=data['password'],
                pic=data['pic'],

            )
            del data
            return render(request,'login.html',{'msg':'Account is Created Successfully:'})
        return render(request,'otp.html',{'msg':'Please Enter Valid OTP '})
    return render(request,'otp.html')

def profile(request):
    return render(request,'profile.html')
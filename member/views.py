import email
from django.http import HttpResponse
from django.shortcuts import redirect, render

from myapp.models import *

# Create your views here.


def member_index(request):
    uid = Member.objects.get(email=request.session['memail'])
    gallery = Gallery.objects.all()
    notice = Notice.objects.all()
    return render(request,'member-index.html',{'uid':uid,'gallery':gallery,'notice':notice})



def member_login(request):
    try:
        uid = Member.objects.get(email=request.session['memail'])
        return redirect('member-index')
    except:
        if request.method == 'POST':
            try:
                uid = Member.objects.get(email=request.POST['email'])
                if request.POST['password'] == uid.password:
                    request.session['memail'] = request.POST['email']
                    return redirect('member-index')
                return render(request,'login.html',{'msg':'Please Enter Valid Password'})
            except:
                msg = 'Email is Not Register '
                return render(request,'login.html',{'msg':msg})
    return render(request,'member-login.html')





def member_logout(request):
    del request.session['memail']
    return redirect('member-login')



def member_profile(request):
    uid = Member.objects.get(email=request.session['memail'])
    return render(request,'member-profile.html',{'uid':uid})
from django.http import HttpResponse
from django.shortcuts import redirect, render

from myapp.models import *

# Create your views here.


def member_index(request):
    memail = request.session.get('memail')
    if not memail:
        return redirect('member-login')
    try:
        uid = Member.objects.get(email=memail)
    except Member.DoesNotExist:
        request.session.pop('memail', None)
        return redirect('member-login')
    gallery = Gallery.objects.all()
    notice = Notice.objects.all()
    return render(request,'member-index.html',{'uid':uid,'gallery':gallery,'notice':notice})



def member_login(request):
    try:
        uid = Member.objects.get(email=request.session['memail'])
        return redirect('member-index')
    except Exception:
        if request.method == 'POST':
            try:
                uid = Member.objects.get(email=request.POST['email'])
                if request.POST['password'] == uid.password:
                    request.session['memail'] = request.POST['email']
                    return redirect('member-index')
                return render(request,'member-login.html',{'msg':'Please Enter Valid Password'})
            except Exception:
                msg = 'Email is Not Register '
                return render(request,'member-login.html',{'msg':msg})
    return render(request,'member-login.html')





def member_logout(request):
    request.session.pop('memail', None)
    return redirect('member-login')



def member_profile(request):
    memail = request.session.get('memail')
    if not memail:
        return redirect('member-login')
    try:
        uid = Member.objects.get(email=memail)
    except Member.DoesNotExist:
        request.session.pop('memail', None)
        return redirect('member-login')
    return render(request,'member-profile.html',{'uid':uid})

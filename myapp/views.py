from django.http import JsonResponse
from random import choices, randrange
import re
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail
from json import loads
from myapp.models import *

# Create your views here.

def index(request):
    uid=Secretary.objects.get(email=request.session['email'])
    
    return render(request,'index.html',{'uid':uid})




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

            )
            del data
            return render(request,'login.html',{'msg':'Account is Created Successfully:'})
        return render(request,'otp.html',{'msg':'Please Enter Valid OTP '})
    return render(request,'otp.html')





def profile(request):
    uid=Secretary.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.email = request.POST['email']
        uid.phone = request.POST['phone']
        uid.address = request.POST['address']
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()

    return render(request,'profile.html',{'uid':uid})





def forgot_password(request):
    if request.method == 'POST':
        try:
            uid = Secretary.objects.get(email=request.POST['email'])
            password = ''.join(choices('abcdefghijklmnopqrstuvwxyz0123456789',k=8))
            subject = 'Reset Password'
            message = f"""Hello {uid.name},
            Your New Password  is {password}"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            uid.password = password
            uid.save()
            return JsonResponse({'msg':'New Password Is Sent On Your Register Email'})
        except:
            msg = 'Email Is Not Register,Please Register First'
            return JsonResponse({'msg':msg})
    return render(request,'forgot-password.html')




def add_house(request):
    if request.method == 'POST':
        House.objects.create(
            room_no = request.POST['room_no'],
            image = request.FILES['image'],
        )
        msg="House is created Succesfully"
        return render(request,'add-house.html',{'msg':msg})
    return render(request,'add-house.html')





def view_house(request):
    uid = House.objects.all()
    return render(request,'view-house.html',{'uid':uid})




def house_edit(request,pk):
    uid = House.objects.get(id=pk)
    if request.method == 'POST':
        uid.room_no = request.POST['room_no']
        if 'image' in request.FILES:
            uid.image = request.FILES['image']
        uid.save()
        msg = "Successfully Updated "
        return render(request,'house-edit.html',{'msg':msg,'uid':uid})
    return render(request,'house-edit.html',{'uid':uid})




def house_delete(request,pk):
    house = House.objects.get(id=pk)
    house.delete()
    return redirect('view-house')





def create_member(request):
    uid = House.objects.all()
    if request.method == 'POST':
        try:
            Member.objects.get(email=request.POST['email'])
            msg = 'Email Is Already Exists In Member'
            return render(request,'create-member.html',{'msg':msg})
        except:
            password = ''.join(choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',k=8))
            subject = 'welcome to Digital Society'
            message = f"""Hello {request.POST['name']},
            Your Username is  {request.POST['email']},
            Your Password is {password} """
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            uid = House.objects.get(room_no=request.POST['room_no'])
            Member.objects.create(
                house = uid,
                name = request.POST['name'],
                email = request.POST['email'],
                phone = request.POST['phone'],
                password = password,
                doc = request.POST['doc'],
                doc_number = request.POST['doc_number'],
                address = request.POST['address'],
            )
    return render(request,'create-member.html',{'uid':uid})




def view_member(request):
    uid = Member.objects.all()
    return render(request,'view-member.html',{'uid':uid})



def edit_member(request,pk):
    uid =Member.objects.get(id=pk)
    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.email = request.POST['email']
        uid.phone = request.POST['phone']
        uid.doc = request.POST['doc']
        uid.doc_number = request.POST['doc_number']
        uid.address = request.POST['address']
        uid.save()
    return render(request,'edit-member.html',{'uid':uid})



def delete_member(request,pk):
    member = Member.objects.get(id=pk)
    member.delete()
    return redirect('view-member')




def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            contact_no = request.POST['contact_no']
        )
        msg ='Successfully Contact Added '
        return render(request,'contact.html',{'msg':msg})
    return render(request,'contact.html')



def contact_view(request):
    uid = Contact.objects.all()
    return render(request,'contact-view.html',{'uid':uid})


def contact_edit(request,pk):
    uid = Contact.objects.get(id=pk)
    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.email = request.POST['email']
        uid.contact_no = request.POST['contact_no']
        uid.save()
    return render(request,'contact-edit.html',{'uid':uid})



def contact_delete(request,pk):
    contact = Contact.objects.get(id=pk)
    contact.delete()
    return redirect('contact-view')




def event_gallery(request):
    if request.method == 'POST':
        Gallery.objects.create(
            name = request.POST['name'],
            image = request.FILES['image']
        )
        msg='Sucessfully Event Is Added '
        return render(request,'event-gallery.html',{'msg':msg})
    return render(request,'event-gallery.html')




def event_gallery_view(request):
    uid = Gallery.objects.all()
    return render(request,'event-gallery-view.html',{'uid':uid})



def event_gallery_edit(request,pk):
    uid = Gallery.objects.get(id=pk)
    if request.method == 'POST':
        uid.name = request.POST['name']
        if 'image' in request.FILES:
            uid.image = request.FILES['image']
        uid.save()
    return render(request,'event-gallery-edit.html',{'uid':uid})



def event_gallery_delete(request,pk):
    gallery = Gallery.objects.get(id=pk)
    gallery.delete()
    return redirect('event-gallery-view')




def notice(request):
    return render(request,'notice.html')



def notice_view(request):
    uid = Notice.objects.all()
    return render(request,'notice-view.html',{'uid':uid})


def notice_edit(request,pk):
    uid = Notice.objects.get(id=pk)
    return render(request,'notice-edit.html',{'uid':uid})


def notice_delete(request,pk):
    notice = Notice.objects.get(id=pk)
    notice.delete()
    return redirect('notice-view')
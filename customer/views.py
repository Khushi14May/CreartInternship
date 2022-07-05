from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def email(request):
	return render(request,'customer/email.html')

def email_info(request):
	thank = False
	myto=request.POST['to']
	mysubject=request.POST['subject']
	mymessage=request.POST['message']
	send_mail(mysubject,mymessage,settings.EMAIL_HOST_USER,[myto],fail_silently=False)
	thank = True
	return render(request,'customer/email.html',{'thank':thank})

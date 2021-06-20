from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import Email
# Create your views here.
def home(request):
    if request.method=="POST":
        par_name = request.POST["par_name"]
        par_email = request.POST["par_email"]
        files = request.FILES 
        par_cer = files["par_cerf"]
        obj = Email.objects.create(par_name=par_name,par_email=par_email,par_cerf=par_cer,par_event='Fastest Fingers First')
        message="Dear "+par_name+',\n\n'+'\tGreetings of the day. We appreciate your presence in the event "WebHacks 1.0" and as a token of appreciation we are attaching a certificate over the same.\n\n \tWe expect the same active participation in our upcoming events from GeeksforGeeks IIITKottayam. Thank you and Enjoy your day. \n We are also in talks with GeeksforGeeks to process your Discount Vouchers soon. We hope you will enjoy the gift from GeeksforGeeks and use it to grow your learning curve. \n\nRegards,\n GeeksforGeeks - IIITKottayam, \nIndian Institute of Information Technology, Kottayam,\nValavoor P.O, Pala,\nKottayam, Kerala.\nPin: 686635\n'
        email = EmailMessage('Appreciation Certificate -- WebHacks 1.0',message,'avsadityavardhan18bcs@iiitkottayam.ac.in',[par_email])
        email.attach_file(obj.par_cerf.file.name)
        email.send()
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Mail Send successfully to '+par_name)
        return redirect('/')
    else:
        return render(request,'send_certificates.html')
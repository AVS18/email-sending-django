from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import Email,BulkExcel
from django.core.files.uploadedfile import InMemoryUploadedFile
import io

# Create your views here.
def home(request):
    if request.method=="POST":
        par_name = request.POST["par_name"]
        par_email = request.POST["par_email"]
        files = request.FILES 
        par_cer = files["par_cerf"]
        obj = Email.objects.create(par_name=par_name,par_email=par_email,par_cerf=par_cer,par_event='Volunteer Cloud and BA')
        message="Dear "+par_name+',\n\n'+'\tGreetings of the day. We appreciate your volunteering in the event "Cloud Computing & Business Analytics" and as a token of appreciation we are attaching a participation certificate over the same.\n\n \tWe expect the same active participation in our upcoming events from IEEE - IIITKottayam. Thank you and Enjoy your day. \n\nRegards,\n IEEE - IIITKottayam, \nIndian Institute of Information Technology, Kottayam,\nValavoor P.O, Pala,\nKottayam, Kerala.\nPin: 686635\n'
        email = EmailMessage('Volunteer Certificate -- Cloud Computing',message,'avsadityavardhan18bcs@iiitkottayam.ac.in',[par_email],cc=['mathewcd@iiitkottayam.ac.in','ieee@iiitkottayam.ac.in'])
        email.attach_file(obj.par_cerf.file.name)
        email.send()
        storage = messages.get_messages(request)
        storage.used = True
        messages.info(request,'Mail Send successfully to '+par_name)
        return redirect('/')
    else:
        return render(request,'send_certificates.html')

import xlrd
import shutil
import os
def sendBulk(request):
    if request.method=="POST":
        files = request.FILES
        excel_sheet = files["excel_sheet"]
        obj = BulkExcel.objects.create(excel_sheet=excel_sheet)
        loc = obj.excel_sheet.file
        wb = xlrd.open_workbook(str(loc))
        sheet = wb.sheet_by_index(0)
        for i in range(1,sheet.nrows):
            print(i,"Started")
            par_name = sheet.cell_value(i,0)
            par_email = sheet.cell_value(i,1)
            file_path = sheet.cell_value(i,2)
            file_name = file_path.split('/')[-1]
            dest_path = os.getcwd()+'/media/cerf/'+file_name
            shutil.copyfile(file_path,dest_path)
            obj = Email.objects.create(par_name=par_name,par_email=par_email,par_cerf=dest_path,par_event='indus-web-again')
            message="Dear "+par_name+',\n\n'+'\tGreetings of the day. We appreciate your participation in the event "Industry Expectations from Budding Engineers" and as a token of appreciation we are attaching a participation certificate over the same.\n\n \tWe expect the same active participation in our upcoming events from ACM IIITKottayam & IIC - IIITKottayam. Thank you and Enjoy your day. \n\nRegards,\n IIC - IIITKottayam, \nIndian Institute of Information Technology, Kottayam,\nValavoor P.O, Pala,\nKottayam, Kerala.\nPin: 686635\n'
            email = EmailMessage('Participation Certificate -- Industry Expectations from Budding Engineers',message,'avsadityavardhan18bcs@iiitkottayam.ac.in',[par_email],cc=['mathewcd@iiitkottayam.ac.in','ragesh@iiitkottayam.ac.in'])
            email.attach_file(obj.par_cerf.file.name)
            email.send()
            print(i,"Completed")
    return render(request,"send_bulk.html")
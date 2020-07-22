  
from django.shortcuts import render

from . import forms
from . import models
# Create your views here.
def  loginpage(request):
    f1=forms.MyForm()
    return render(request,"login.html",{'form':f1})

def getdata(request):
    
    if request.method=='GET':
        u=request.GET['username']
        p=request.GET['password']
        ph=request.GET['phone']
        a=request.GET['address']

        return render(request,'valid.html',{"username":u,"password":p,"phone":ph,"address":a})

    if request.method=='POST':

         u=request.POST['username']
         p=request.POST['password']
         ph=request.POST['phone']
         a=request.POST['address']
         s1=models.Student(username=u,password=p,phone=ph,address=a)
         s1.save() #this will save record to database
         return render(request,'valid.html',{"username":u,"password":p,"phone":ph,"address":a})
         
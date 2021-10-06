from typing_extensions import ParamSpecKwargs
from django.http.response import HttpResponse
from home.models import CustomUser
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check(email):
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return True
 
    else:
        return False
 
# Create your views here.
def index(request):
    return render(request,'index.html')

def signUp(request):
    if request.method=="POST":
        name=request.POST['name']
        company_name=request.POST['company_name']
        email=request.POST['mail']
        username=request.POST['username']
        phone=request.POST['mobile']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect(signUp)

            elif name =='' and company_name=='' and email==''and username=='' and phone=='':
                messages.info(request,'fill all the fields')
                return redirect(signUp)
                
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request,'Mail taken')
                return redirect(signUp)

            elif not check(email):
                messages.info(request,'Invalid mail')
                return redirect(signUp)
            else:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,name=name,phone=phone,company_name=company_name)
                user.save()
                messages.info(request,'Created Successfully')

        else:
            messages.info(request,'passwords not matching')
            return redirect(signUp)
    return render(request,'signup.html')
def loginUser(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        user =auth.authenticate(username=username,password=password)
        print(username,password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')
            return render(request,'login.html')
    return render(request,'login.html')
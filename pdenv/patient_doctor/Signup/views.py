from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from Signup.models import Signup
from .forms import SignupForm


# Create your views here.

def index(request):
    if request.method == "POST":
       msg="" 
       username=request.POST.get('username')
       password = request.POST.get('password') 
       #user = authenticate(request,username=username, password= password)
       user = Signup.objects.filter(username= username,password= password)
       if Signup.objects.filter(username=username, password=password).exists():
           newU = Signup.objects.get(username=username, password=password)
           if newU.role=="patient":
                  return render(request,"dashboard_pt.html",{'patient':newU})
           else:
                
                return render(request,"dashboard_dt.html",{'doctor':newU})
       else:
            
           msg = "INVALID USERNAME OR PASSWORD"
           #return redirect("/loginIN")
           return  render(request,'index.html',{'msg':msg})
    return  render(request,'index.html')
    """ if user is not None:
           for users in user:
             print(users.role)     
             if users.role=="patient":
                  return render(request,"dashboard_pt.html",{'patient':users})
             else:
                
                return render(request,"dashboard_dt.html",{'doctor':users})
        
       else:
        
           msg = "INVALID USERNAME OR PASSWORD"
           #return redirect("/loginIN")
           return  render(request,'start.html',{'msg':msg})
    return  render(request,'start.html')"""
    #return render(request,"index.html")
    #return HttpResponse("welcome")

def dashboard_pt(request):
    return render(request,"dash.html")    

def dashboard_dt(request): 
    return render(request,"dashboard_dt.html")    
"""def register(request):
    if request.method == "POST":
      msg="" 
      fname=request.POST.get('fname')
      lname = request.POST.get('lname') 
     
      username=request.POST.get('username')
      password = request.POST.get('password') 
      conf = request.POST.get('conf') 
      
      role=request.POST.get('role')
      email=request.POST.get('eid')
      address = request.POST.get('add') 
      
      city=request.POST.get('city')
      state = request.POST.get('State') 
      
      pincode=request.POST.get('Pincode')
      #pic = request.FILES
      pic = request.POST.get('pic') 
      if(password==conf):
        newuser=Signup(first_name=fname,last_name=lname,username=username,password=password,confirm_password=conf,role=role,email=email,address=address,city=city,state=state,pincode=pincode,pic=pic)
        newuser.save()
        return redirect("/")
      else:
         # No backend authenticated the credentials
           msg = "PASSWORD AND CONFIRM_PASSWORD DO NOT MATCHED,PLEASE ENTER IT AGAIN"
           #return redirect("/loginIN")
           return  render(request,'reg.html',{'msg':msg})
    return  render(request,'reg.html')
    """
def reg(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():
            first_name= form.cleaned_data.get('first_name')
            last_name= form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')            
            confirm_password= form.cleaned_data.get('confirm_password')
            role= form.cleaned_data.get('role')
            email = form.cleaned_data.get('email')
            address= form.cleaned_data.get('address')
            pincode= form.cleaned_data.get('pincode')
            state= form.cleaned_data.get('state')
            city= form.cleaned_data.get('city')
            pic= form.cleaned_data.get('pic')
            
            if password==confirm_password:
               # Create user
               #newUser = Signup(first_name=first_name,last_name=last_name,username=username, password=password,confirm_password=confirm_password,role=role,email=email, address=address,pincode=pincode,state=state,city=city,pic=pic)
               #newUser.save()
               form.save()
               return redirect('/')
            else :
                 msg = "PASSWORD AND CONFIRM_PASSWORD DO NOT MATCHED,PLEASE ENTER IT AGAIN"
                 form = SignupForm()  
                 return  render(request,'sign.html',{'msg':msg,'form': form})
    else:
        form = SignupForm()
    return render(request, 'sign.html', {'form': form})

def display(request):
    
    #if request.method == 'POST':

        # getting all the objects of hotel.
        Hotels = Signup.objects.all()
        return  render(request,'display.html',{'Hotels':Hotels})
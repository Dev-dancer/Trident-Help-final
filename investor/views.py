from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model 
# from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_tobe
from django.contrib.auth import logout as logout_tobe
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import User
from .forms import UserForm
from django.contrib import messages
from django.db.models import Max,Min
User=get_user_model()

# Create your views here.

def main(request):
    return render(request,'investor/main.html')


# invest in investor
from django.shortcuts import render, redirect
from django.contrib import messages
from investor.models import UserProfile 

@login_required
def investment(request):
    if request.method == 'POST':
        amt = request.POST.get('amt')
        interest = request.POST.get('interest')
        user_profile=UserProfile(user=request.user,amt=amt,interest=interest)
        user_profile.save()
        
        return redirect('investor:success')
    
        
    
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None
    
    return render(request, 'investor/invest.html', {'user_profile': user_profile})


def investment_details(request):
    investor=UserProfile.objects.all()
    min_price=UserProfile.objects.all().aggregate(Min('amt'))
    max_price=UserProfile.objects.all().aggregate(Max('amt'))
    # print("HEY")
    # print(min_price)
    Filterprice=request.GET.get('Filterprice')
    if Filterprice:
        Int_filterPrice=int(Filterprice)
        investor=UserProfile.objects.filter(amt__lte=Int_filterPrice)
    else:
        investor=UserProfile.objects.all()
        
    return render(request,'investor/investor.html',{'investor':investor})


# def register(request):
#     if request.method=='POST':
#         form=UserForm( request.POST)
#         if form.is_valid():
#             password=form.cleaned_data['password']   
#             user=form.save(commit=False)
#             user.set_password(password)
#             # user=form.save(commit=False)
#             # form.save()
#             # username=form.cleaned_data.get('username')
#             # messages.success(request,f'Welcome {username}, your account is created')
            
#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             email=form.cleaned_data['email']
#             password=form.cleaned_data['password']
#             phone_number=form.cleaned_data['phone_number']
#             user=User.objects.create_user(first_name=first_name,last_name=last_name,phone_number=phone_number,password=password,email=email)
#             user.save()
#             # username=form.cleaned_data.get('username')
#             # messages.success(request,f'Welcome {username}, your account is created')
#             form.save()
#             return redirect('investor:login')
            
#     else:
#         # print("NOT WORKING")
#         form=UserForm()

#     return render(request,'investor/register.html',{'form':form})


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save() 
            return redirect('investor:login')
        # print(request.POST)
    else:
        form = UserForm()
    return render(request,'investor/register.html',{'form':form})


def login(request):
    if request.method=="POST":
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        user = authenticate(phone_number=phone_number, password=password) 
        if user is not None:
            # print("hey")
            login_tobe(request,user)
            # return redirect('investor:main')
            return redirect('investor:login')
            
            
        else:
            # print("Bye")
            # return redirect('investor:investor')
            return redirect('investor:investment')
            
    else:
        return render(request,'investor/login.html',{})

def success(request):
    return render(request,'investor/successful.html',{})
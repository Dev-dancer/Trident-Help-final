from django.shortcuts import render,redirect
# from django.contrib.auth import get_user_model 
# from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_tobe
from django.contrib.auth import logout as logout_tobe
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from investor.models import User
from investor.models import UserProfile
from investor.forms import UserForm
from .forms import clerkform
from django.db.models import Max,Min

# from django.contrib.auth.forms import UserCreationForm

# #use for user reg
# def registerClerk(request):
#     if request.method=='POST':
#         form=UserForm(request.POST)
#         c_form=clerkform(request.POST)
#         if form.is_valid() and c_form.is_valid():
#             first_name=form.cleaned_data['first_name']
#             last_name=form.cleaned_data['last_name']
#             password=form.cleaned_data['password']
#             user=User.objects.create_user(first_name=first_name,last_name=last_name,password=password)
#             user.save()
#             clerk=c_form.save(commit=False)
#             clerk.user=user
#             clerk.save()
#     else:
#         form=UserForm()
#         c_form=clerkform()
    
#     context={
#         'form':form,
#         'c_form':c_form,
#     }
#     return render(request,'clerk/registerClerk.html',context)

def loginClerk(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        password=password.POST['password']

        user=authenticate(first_name=first_name,password=password)
        if user is not None:
            login_tobe(request,user)
            return redirect('clerk:dashboard')
        else:
            return redirect('clerk:loginClerk')
    return render(request,'clerk/login.html')

def dashboard(request):
    return render(request,'clerk/dashboard.html')

# def login_patient(request):
#     if request.method=="POST":
#         username=request.POST['username']
        
# def logout_patient(request):

def register_user(request):
    if request.method =="POST":
    #     form=UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username=form.cleaned_data['username']
    #         password=form.cleaned_data['password1']
    #         user=authenticate(username=username,password=password)
    #         login(request,user)
    #         messages.success(request,("Registration successful"))
    #         return redirect('')
    # else:
    #     form=UserCreationForm()
    # return render(request, 'clerk/registeruser.html',{'form':form})
    
        form = UserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()  
            return redirect('clerk:dashboard')
    else:
        form = UserForm()
    return render(request,'clerk/user_registration.html',{'form':form})


    # if request.method == 'POST':
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     father_name = request.POST.get('father_name')
    #     mother_name = request.POST.get('mother_name')
    #     gender = request.POST.get('gender')
    #     pan_number = request.POST.get('pan_number')
    #     mobile_number = request.POST.get('mobile_number')
    #     occupation = request.POST.get('occupation')
    #     income = request.POST.get('income')
    #     address = request.POST.get('address')
    #     pincode = request.POST.get('pincode')
     
    #     return redirect('clerk:dashboard')  
    # return render(request, 'clerk/user_registration.html')
    

def dash_to_userreg(request):
    return render(request,'clerk/user_registration.html',{})


def dash_to_ourfund(request):
    return render(request,'clerk/ourfund.html',{})
    
def ourfundtosuccess(request):
    return render(request,'clerk/succespage.html',{})

def succestohome(request):
    return render(request,'main/main_page.html',{})

def dashtoloi(request):
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


def loitosucc(request):
    return render(request,'clerk/list of inv success.html',{})



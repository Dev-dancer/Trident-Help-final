from django.shortcuts import render,redirect

def main_page(request):
    return render(request,'main/homepage.html',{})

def toabtpage(request):
    return render(request,'main/about_us.html',{})


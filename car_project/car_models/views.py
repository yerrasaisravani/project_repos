from django.shortcuts import render,redirect
from car_models.models import CarDetails 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout 
# Create your views here.
def loginview(request):
    if request.user.is_authenticated:
        messages.warning(request,"You already Logged in ")
        return redirect('car')
    if request.method=="POST":
        userName=request.POST.get('username')
        passWord=request.POST.get('password')
        user=authenticate(username=userName,password=passWord,is_active=True)
        if user is not None:
            login(request,user)
            messages.success(request,"You {} are successfully Looged In".format(user.username))
            return redirect('car')
        else:
            messages.error(request,"You enter wrong Username or Password")
            return render(request,'login.html')
    return render(request,'login.html') 
@login_required(login_url='login')
def table_view(request):
    records=CarDetails.objects.all()
    context={'data':records}
    if request.method=='POST':
        car_name=request.POST.get('car_name')
        car_year=int(request.POST.get('car_year'))
        car_color=request.POST.get('car_color')
        obj=CarDetails(name=car_name,year=car_year,color=car_color)
        obj.save()
        messages.info(request,"You are successfully Added..")
        return redirect('car')
    return render(request,'cars.html',context)
def logout_view(request):
    logout(request)
    messages.warning(request,"Hey you are logout .. ")
    return redirect('login')
def Update_view(request):
    if request.method=='POST':
        pk=int(request.POST.get('car_id'))
        car_name=request.POST.get('car_name')
        if CarDetails.objects.filter(id=pk).exists():
            obj=CarDetails.objects.get(id=pk)
            obj.name=car_name
            obj.save()
            messages.info(request,"You are successfully Updated..")
            return redirect('car')
        else:
            messages.error(request,"You are entered data not Found..")
            return redirect('update')
    return render(request,'update.html')
def Delete_view(request,pk):
    if request.method=='POST':
        pk=int(request.POST.get('car_id'))
        if CarDetails.objects.filter(id=pk).exists():
            obj=CarDetails.objects.get(id=pk)
            obj.delete()
            messages.success(request,"You are successfully deleted ")
            return redirect('car')
        else:
            messages.warning(request,"You are entered data not found..")
            return redirect('delete')
    return render(request,'remove.html')
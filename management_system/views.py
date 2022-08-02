
from django.shortcuts import render,redirect,HttpResponse
from sms_app.email_backend import EmailBackend
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from sms_app.models import CustomUser
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request,'base.html')

def login_user(request):
    return render(request,'login.html')


def userLogin(request):
    if request.method == 'POST':

        user = EmailBackend.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))

        if user != None:
            login(request,user)
            user_type = user.user_type

            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                 return redirect('staff_home')
            elif user_type == '3':
                 return redirect('student_home')
            else:
                messages.error(request,'Email or Password are Invalid!!')
                return redirect('login')
        else:
            messages.error(request,'Email or Password are Invalid!!')
            return redirect('login')
        
def userLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def update_profile(request):
    user = CustomUser.objects.get(id= request.user.id)
    context = {'user':user}
    return render(request,'update_profile.html',context) 

@login_required(login_url='login')
def profile_update_form(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        # email  = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_pic = request.FILES.get('profile_pic')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            

            if password != None and password != "":
                customuser.set_password(password)
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,'Successfully Update your Profile!')
            return redirect('update_profile')
        except:
            messages.error(request,'Failed to Update your Profile !!')

    return render(request, 'update_profile.html')


from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from requests import session
from django.contrib import messages
from sms_app.models import Student,Course,SessionYear,CustomUser,Staff,Subject,Notification,StaffLeave,Feedback,StudentNotification


def home(request):
    return render(request,'student/home.html') 

def see_notification(request):
    stu = Student.objects.filter(user=request.user.id)

    student = Student.objects.get(user=stu)
    message = StudentNotification.objects.filter(student=student)

    context = {
        'notification': message,
    }
    return render(request, 'student/see_notification.html',context)

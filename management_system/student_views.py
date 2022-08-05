
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from requests import session
from django.contrib import messages
from sms_app.models import Student,Course,SessionYear,CustomUser,Staff,Subject,Notification,StaffLeave,Feedback,StudentNotification,StudentFeedback,StudentLeave


def home(request):
    return render(request,'student/home.html') 

def student_notification(request):
    current_user = Student.objects.get(user=request.user.id)
   
    student_notification_list = StudentNotification.objects.filter(student=current_user).order_by('-created_at')
    context = {'student_notificaion_list':student_notification_list}
    return render(request, 'student/student_notification.html',context )   


def seen_student_notification(request,id):
    notification = StudentNotification.objects.get(id=id) 
    notification.status = 1
    notification.save() 
    return redirect('student_notification')


def student_feedback(request):
    student = Student.objects.get(user=request.user.id) 
    feedback = StudentFeedback.objects.filter(student=student) 

    return render(request, 'student/student_feedback.html',{'feedback':feedback})  

def send_student_feedback(request):
    if request.method == 'POST':
        msg = request.POST.get('message') 
        student = Student.objects.get(user=request.user.id) 
        feedback = StudentFeedback(
            student = student,
            feedback_msg = msg,
        )
        feedback.save() 
        messages.success(request,'Feedback Send Successfully!')
        return redirect('student_feedback') 

def student_leave(request):
    student = Student.objects.get(user=request.user.id) 
    student_leave = StudentLeave.objects.filter(student=student) 
    context = {'student_leave':student_leave}
    return render(request, 'student/student_leave.html',context)  

def student_leave_save(request):
    if request.method == 'POST':
        msg = request.POST.get('leave_message')
        date = request.POST.get('leave_date')
        student = Student.objects.get(user=request.user.id) 
        leave = StudentLeave(
            student=student,
            leave_date = date,
            message = msg,

        )
        leave.save() 
        messages.success(request,'Send Leave Request Successfully!') 
        return redirect('student_leave')


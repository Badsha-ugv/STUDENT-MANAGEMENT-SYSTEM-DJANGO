
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from requests import session
from django.contrib import messages

from sms_app.models import Student,Course,SessionYear,CustomUser,Staff,Subject,Notification,StaffLeave,Feedback,StudentNotification,StudentFeedback,StudentLeave,AttendanceReport,TakeAttendance,StudentResult


def home(request):
    return redirect('hod_home')


@login_required(login_url='/')
def student_notification(request):
    current_user = Student.objects.get(user=request.user.id)
   
    student_notification_list = StudentNotification.objects.filter(student=current_user).order_by('-created_at')
    context = {'student_notificaion_list':student_notification_list}
    return render(request, 'student/student_notification.html',context )   


@login_required(login_url='/')
def seen_student_notification(request,id):
    notification = StudentNotification.objects.get(id=id) 
    notification.status = 1
    notification.save() 
    return redirect('student_notification')

@login_required(login_url='/')
def student_feedback(request):
    student = Student.objects.get(user=request.user.id) 
    feedback = StudentFeedback.objects.filter(student=student) 

    return render(request, 'student/student_feedback.html',{'feedback':feedback})  

@login_required(login_url='/')
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

@login_required(login_url='/')
def student_leave(request):
    student = Student.objects.get(user=request.user.id) 
    student_leave = StudentLeave.objects.filter(student=student) 
    context = {'student_leave':student_leave}
    return render(request, 'student/student_leave.html',context)  


@login_required(login_url='/')
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

@login_required(login_url='/')
def view_attendance_student(request):
    student = Student.objects.get(user=request.user.id) 
    subject = Subject.objects.filter(course = student.course_name)

    action = request.GET.get('action') 
    get_subject = None 
    attendance_report = None 
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id') 
            get_subject = Subject.objects.get(id=subject_id) 

            attendance_report = AttendanceReport.objects.filter(student=student,attendance__subject=subject_id).order_by('-id')
    context = {
        'subject':subject,
        'action':action,
        'get_subject':get_subject,
        'attendance_report':attendance_report,
        }
    return render(request, 'student/view_student_attendance.html',context)  

@login_required(login_url='/')
def view_result(request):
    student = Student.objects.get(user=request.user.id) 
    result = StudentResult.objects.filter(student=student) 
    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark 
        total_mark = assignment_mark + exam_mark

    context = {
        'result':result,
        'total_mark':total_mark,
    }
    return render(request,'student/view_result.html',context)  
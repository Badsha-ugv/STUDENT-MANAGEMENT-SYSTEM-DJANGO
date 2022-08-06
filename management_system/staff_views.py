
from django.shortcuts import render,redirect
from sms_app.models import Staff,Notification,StaffLeave,Feedback,Subject,SessionYear
from django.contrib import messages

def staff_home(request):

    return render(request,'staff/staff_home.html') 

def staff_notification(request):
    current_stuff = Staff.objects.get(user=request.user.id) 
    staff_notification_list = Notification.objects.filter(staff=current_stuff) 
    context = {'staff_notification':staff_notification_list}
    return render(request, 'staff/view_staff_notification.html',context)  

def seen_staff_notification(request,id):
    staff_notification = Notification.objects.get(id=id) 
    staff_notification.status = 1
    staff_notification.save()
    return redirect('staff_notification')

def staff_leave(request):
    stafff = Staff.objects.filter(user=request.user.id) 
    for i in stafff:
        staff_id = i.id
        staff_leave = StaffLeave.objects.filter(staff=staff_id).order_by('-id')

    context = {'staff_leave':staff_leave}    
    return render(request, 'staff/staff_leave.html' ,context) 


def staff_leave_save(request):    
    if request.method == 'POST':
        date = request.POST.get('leave_date')
        message = request.POST.get('leave_message')
        staff = Staff.objects.get(user=request.user.id)
        leave = StaffLeave(
            staff = staff,
            leave_date = date,
            message = message,
        )
        leave.save() 
        messages.success(request,'Leave Reques Sent Successfully!') 
        return redirect('staff_leave')

def send_feedback(request):
    staff = Staff.objects.get(user=request.user.id) 
     
    feedback = Feedback.objects.filter(staff=staff) 
    context = {'feedback':feedback} 

    return render(request, 'staff/feedback.html',context)  

def save_feedback_msg(request):
    if request.method == 'POST':
        message = request.POST.get('message') 
        staff = Staff.objects.get(user=request.user.id) 
        feedback = Feedback(
            staff = staff,
            feedback_msg = message,

        )
        feedback.save() 
        messages.success(request,'Feedback Message Sent!') 
        return redirect('send_feedback') 
    return redirect('send_feedback') 

def take_attendance(request):
    staff = Staff.objects.get(user=request.user.id) 
    subject = Subject.objects.filter(staff=staff) 
    session = SessionYear.objects.all() 
    context = {
        'subject':subject,
        'session':session,
    }
    return render(request,'staff/take_attendance.html',context)   
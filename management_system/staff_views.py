
from django.shortcuts import render,redirect
from sms_app.models import Staff,Notification,StaffLeave,Feedback
from django.contrib import messages

def staff_home(request):

    return render(request,'staff/staff_home.html') 

def notification(request):
    curret_user = request.user.id
    staff_id = Staff.objects.filter(user= curret_user)
    for i in staff_id:
        staff = i.id
        # print(staff_id)
        notifications = Notification.objects.filter(staff=staff)
        context = {'notification': notifications}
        return render(request, 'staff/view_notification.html',context)

def msg_seen(request,id):

    notification = Notification.objects.get(id=id) 
    notification.status = 1
    notification.save()
    return redirect('notification')

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
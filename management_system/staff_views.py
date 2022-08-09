
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from sms_app.models import Staff,Notification,StaffLeave,Feedback,Subject,SessionYear,Student,TakeAttendance,AttendanceReport,StudentResult
from django.contrib import messages


def staff_home(request):

    return redirect('hod_home')

@login_required(login_url='/')
def staff_notification(request):
    current_stuff = Staff.objects.get(user=request.user.id) 
    staff_notification_list = Notification.objects.filter(staff=current_stuff) 
    context = {'staff_notification':staff_notification_list}
    return render(request, 'staff/view_staff_notification.html',context)  


@login_required(login_url='/')
def seen_staff_notification(request,id):
    staff_notification = Notification.objects.get(id=id) 
    staff_notification.status = 1
    staff_notification.save()
    return redirect('staff_notification')

@login_required(login_url='/')
def staff_leave(request):
    stafff = Staff.objects.filter(user=request.user.id) 
    for i in stafff:
        staff_id = i.id
        staff_leave = StaffLeave.objects.filter(staff=staff_id).order_by('-id')

    context = {'staff_leave':staff_leave}    
    return render(request, 'staff/staff_leave.html' ,context) 


@login_required(login_url='/')
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

@login_required(login_url='/')
def send_feedback(request):
    staff = Staff.objects.get(user=request.user.id) 
     
    feedback = Feedback.objects.filter(staff=staff) 
    context = {'feedback':feedback} 

    return render(request, 'staff/feedback.html',context)  

@login_required(login_url='/')
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

@login_required(login_url='/')
def take_attendance(request):
    staff = Staff.objects.get(user=request.user.id) 
    subjects = Subject.objects.filter(staff=staff) 
    session = SessionYear.objects.all() 
    action = request.GET.get('action') 

    get_subject = None 
    get_session = None 
    students = None 
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session = request.POST.get('session_id') 

            get_subject = Subject.objects.get(id=subject_id)
            get_session = SessionYear.objects.get(id=session)

            subject = Subject.objects.filter(id=subject_id)
            
            for i in  subject:
                student_course = i.course.id
                students = Student.objects.filter(course_name=student_course) 

    context = {
        'subject':subjects,
        'session':session,
        'get_subject':get_subject,
        'get_session':get_session,
        'action':action,
        'students':students,
 
    }
    return render(request,'staff/take_attendance.html',context)   

@login_required(login_url='/')
def save_attendance(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_id = request.POST.get('session_id')
        attendance_date = request.POST.get('attendance_date')
        students_id = request.POST.getlist('students_id') 

        get_subject = Subject.objects.get(id=subject_id)
        get_session = SessionYear.objects.get(id=session_id) 
        attendance = TakeAttendance(
            subject = get_subject,
            session = get_session,
            attendance_date = attendance_date,
        )
        attendance.save() 
        for i in students_id:
            stu = int(i) 
            present_student = Student.objects.get(id=stu) 
            attendance_report = AttendanceReport(
                student = present_student,
                attendance = attendance,
            )
            attendance_report.save() 
            

        return redirect('take_attendance')

@login_required(login_url='/') 
def view_attendance(request):
    staff = Staff.objects.get(user=request.user.id) 
    subject = Subject.objects.filter(staff=staff) 
    session = SessionYear.objects.all() 

    action = request.GET.get('action')

    get_session = None 
    get_subject = None 
    attendance_report = None 
    attendance_date = None 
    
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_id = request.POST.get('session_id')
            attendance_date = request.POST.get('attendance_date') 

            get_subject = Subject.objects.get(id=subject_id)
            get_session = SessionYear.objects.get(id=session_id)

            attendance = TakeAttendance.objects.filter(subject=get_subject,attendance_date=attendance_date) 
            for i in attendance:
                attendance_id  = i.id
                attendance_report = AttendanceReport.objects.filter(attendance=attendance_id) 



    context = {
        'subject':subject,
        'session':session,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session, 
        'attendance_date':attendance_date,
        'attendance_report':attendance_report,

    }
    return render(request,'staff/view_attendance.html',context)  


@login_required(login_url='/')
def add_result(request):
    staff = Staff.objects.get(user=request.user.id) 
    subject = Subject.objects.filter(staff=staff)
    session = SessionYear.objects.all() 

    action = request.GET.get('action') 

    
    get_subject = None 
    get_session = None 
    students = None 
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_id = request.POST.get('session_id')
            print(subject_id)
            print(session_id)
            get_subject = Subject.objects.get(id=subject_id)
            get_session = SessionYear.objects.get(id=session_id)

            subjects = Subject.objects.filter(id=subject_id) 
            print(subjects) 
            print(get_subject) 
            for i in subjects:
                course_id = i.course.id
                students = Student.objects.filter(course_name=course_id)



    context = {
        'subject':subject,
        'session':session,
        'action':action, 
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students,
    }    
    return render(request, 'staff/add_result.html',context)   

@login_required(login_url='/')
def save_student_result(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_id = request.POST.get('session_id')
        student_id = request.POST.get('student_id')
        exam_mark = request.POST.get('exam_mark')
        assignment_mark = request.POST.get('assignment_mark')
        print(student_id) 
        get_student = Student.objects.get(user=student_id) 
        get_subject = Subject.objects.get(id=subject_id) 

        existance = StudentResult.objects.filter(student=get_student,subject=get_subject).exists() 

        if existance:
            result = StudentResult.objects.get(student=get_student,subject=get_subject)
            result.exam_mark = exam_mark
            result.assignment_mark = assignment_mark

            result.save() 
            messages.success(request,'Update Student Result Successfully!')
            return redirect('add_result')
        else: 
            result = StudentResult(
                student = get_student,
                subject = get_subject,
                exam_mark = exam_mark,
                assignment_mark = assignment_mark,

            )
            result.save() 
            messages.success(request,'Add Student Result Successfully!')
            return redirect('add_result')

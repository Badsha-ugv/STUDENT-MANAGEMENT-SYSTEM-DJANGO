

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from requests import session
from django.contrib import messages
from sms_app.models import Student,Course,SessionYear,CustomUser,Staff,Subject,Notification,StaffLeave,Feedback,StudentNotification

@login_required(login_url='/')
def home(request):
    total_student = Student.objects.all().count 
    total_staff = Staff.objects.all().count 
    total_course = Course.objects.all().count 
    total_subject = Subject.objects.all().count

    total_male_student = Student.objects.filter(gender='male').count()
    total_female_student = Student.objects.filter(gender='female').count()

    print(total_female_student)
    print(total_male_student)

    print(total_male_student,total_female_student)

    gender_label = ['Male','Female']
    gender_list = [total_male_student,total_female_student]

    context = {
        'total_student':total_student,
        'total_staff':total_staff,
        'total_course':total_course,
        'total_subject':total_subject,
        'labels':gender_label,
        'data':gender_list,

        
        
    }
    return render(request,'hod/hod_home.html',context)  


@login_required(login_url='/')
def add_student(request):

    return redirect(request,'hod/add_student.html')
    

@login_required(login_url='/')
def add_student(request):
    course = Course.objects.all()
    session_year = SessionYear.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course = request.POST.get('course')
        session_year = request.POST.get('session_year')
        address = request.POST.get('address')
        profile_pic = request.FILES.get('profile_pic')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'This Email Already Taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'This Username Already Taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                profile_pic = profile_pic,
                user_type = 3,
            )
            user.set_password(password)
            user.save()
            course = Course.objects.get(id=course)
            session_year = SessionYear.objects.get(id=session_year)
            student = Student(
                user = user,
                address = address,
                gender = gender,
                course_name = course,
                session_year = session_year,
            )
            student.save()
            messages.success(request,'Student Added Successfylly!')
            return redirect('add_student')


    context = {
        'courses':course,
        'session_year':session_year,
    }
    return render(request,'hod/add_student.html',context) 

@login_required(login_url='login')
def view_student(request):
    student = Student.objects.all()

    context = {
        'students':student,
    }
    return render(request, 'hod/view_student.html',context)


@login_required(login_url='/')
def edit_student(request,id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    session_year = SessionYear.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course')
        session_year_id = request.POST.get('session_year')
        address = request.POST.get('address')
        profile_pic = request.FILES.get('profile_pic')

        user = CustomUser.objects.get(id=user_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if password != None and password != "":
            user.set_password(password)
            

        if profile_pic != None and profile_pic != "":
            user.profile_pic= profile_pic
        
        user.save()

        student = Student.objects.get(user=user_id)
        student.address = address
        student.gender = gender 

        course = Course.objects.get(id=course_id)
        student.course = course

        session_year = SessionYear.objects.get(id=session_year_id)
        student.session_year = session_year

        student.save()

        messages.success(request,'Student added Successfully!')
        return redirect('view_student')
            
        
    context = {
        'students':student,
        'courses':course,
        'session_year':session_year,
    }
    return render(request,'hod/edit_student.html',context) 


@login_required(login_url='/')
def delete_student(request,id):
    student = CustomUser.objects.get(id=id)
    student.delete()
    messages.success(request,'Student Deleted Successfylly!!')
    return redirect('view_student')


@login_required(login_url='/')
def add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request,'Successfully Added the Course!')
        return redirect('add_course') 
    return render(request, 'hod/add_course.html')  


@login_required(login_url='/')
def view_course(request):
    course = Course.objects.all()
    context = {'courses':course}
    return render(request, 'hod/view_course.html',context) 

@login_required(login_url='/')
def update_course(request,id):
    course = Course.objects.get(id=id) 
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course.name = course_name
        course.save() 
        messages.success(request,'Course Update Successfully!')
        return redirect('view_course')
    context = {'course':course} 
    return render(request, 'hod/update_course.html',context) 

@login_required(login_url='/')
def delete_course(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request,'Course Delete Successfully!')
    return redirect('view_course')

def add_staff(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        username = request.POST.get('username')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'This Email is Already Taken')
            return redirect('add_staff')
            
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'This Email is Already Taken')
            return redirect('add_staff')
        else:
            user = CustomUser(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                profile_pic=profile_pic,
                user_type = 2
            )
            user.set_password(password)
            user.save()
            
            staff = Staff(
                user=user,
                address=address,
                gender=gender,
            )
            staff.save()
            messages.success(request,'Add Staff Successfully!')
            return redirect('add_staff') 
    return render(request,'hod/add_staff.html')


@login_required(login_url='/')
def view_staff(request):
    staff = Staff.objects.all() 
    context = {'staff_list':staff}

    return render(request,'hod/view_staff.html',context) 

@login_required(login_url='/') 
def update_staff(request,id):
    staff = Staff.objects.get(id=id) 
    if request.method ==  'POST':  
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        profile_pic = request.FILES.get('profile_pic')
        user_id = request.POST.get('staff_id') 
        password = request.POST.get('password')
        user = CustomUser.objects.get(id=user_id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email 
        
        if password != None and password != "":
            user.set_password(password)

        if profile_pic != None and profile_pic != '':
            user.profile_pic = profile_pic 
        user.save() 

        staff = Staff.objects.get(user = user_id) 
        staff.address  = address
        staff.gender = gender 
        staff.save()
        messages.success(request, 'Update Staff Info Successfully!') 
        return redirect('view_staff') 

    context = {'staff':staff}
    return render(request, 'hod/update_staff.html',context) 

@login_required(login_url='/') 
def delete_staff(request,id):
    staff = CustomUser.objects.get(id=id)
    staff.delete() 
    messages.success(request,'Delete Staff Successfully!') 
    return redirect('view_staff') 


def add_subject(request):
    staff = Staff.objects.all() 
    course = Course.objects.all() 

    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        staff_id = request.POST.get('staff')
        course_id = request.POST.get('course')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subjct = Subject(
            name = subject_name,
            staff = staff,
            course = course,
        )
        subjct.save() 
        messages.success(request,'Subject Added Successfully!') 
        return redirect('add_subject') 
    context = {
        'courses':course,
        'staff_list':staff,
    }
    return render(request,'hod/add_subject.html',context)  


def view_subject(request):
    subject = Subject.objects.all() 
    
    context = {'subjects':subject} 
    return render(request,'hod/view_subject.html',context) 

def edit_subject(request,id):
    subject = Subject.objects.get(id=id) 
    staff   = Staff.objects.all()
    course   = Course.objects.all()
    
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        staff_id = request.POST.get('staff')
        course_id = request.POST.get('course')

        staff = Staff.objects.get(id=staff_id)
        course = Course.objects.get(id=course_id)

        subject = Subject.objects.get(id=id) 
        subject.name = subject_name
        subject.staff = staff 
        subject.course = course 
        subject.save() 
        messages.success(request,'Subject Updated Successfully!')
        return redirect('view_subject') 
    
    context = {'subject':subject,
    'staff_list':staff,
    'courses':course,
    } 
    return render(request,'hod/edit_subject.html',context)  

def delete_subject(request,id):
    subject = Subject.objects.get(id=id) 
    subject.delete() 
    messages.success(request,'Subject Deleted Successfully!') 
    return redirect('view_subject') 

# Session

def add_session(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_session')
        end_date = request.POST.get('end_session')

        session = SessionYear(
            start_date = start_date,
            end_date = end_date
        )
        session.save() 
        messages.success(request,'Sesion Added Successfully!') 
        return redirect('add_session') 


    return render(request,'hod/add_session.html') 

def view_session(request):
    session = SessionYear.objects.all() 
    context = {'session':session}
    return render(request, 'hod/view_session.html',context) 

def update_session(request,id):
    session = SessionYear.objects.get(id=id)

    if request.method == 'POST':
        start_date = request.POST.get('start_session')
        end_date = request.POST.get('end_session')

        session.start_date = start_date
        session.end_date = end_date
        session.save() 
        messages.success(request,'Session Updated Successfully!') 
        return redirect('view_session') 
    context = {'session':session} 
    return render(request, 'hod/update_session.html',context)  

def delete_session(request,id):
    session = SessionYear.objects.get(id=id) 
    session.delete() 
    messages.success(request,'Session Delete Successfully!') 
    return redirect('view_session') 
    
def notification(request):
    staff = Staff.objects.all() 
    notification = Notification.objects.all().order_by('-id')[:5]
    
    if request.method == 'POST':
        message = request.POST.get('msg')
        staff_id = request.POST.get('staff_id') 

        staff = Staff.objects.get(user=staff_id) 

        notification = Notification(
            staff = staff,
            message = message,
            
            
        )
        notification.save()
        messages.success(request,'Notificatin Sent Successfully!')
        return redirect('staff_notification') 


    context = {'staff_list':staff,'notifications':notification} 
    return render(request, 'hod/notification.html',context)  


def staff_leave_request(request):
    leave_request = StaffLeave.objects.all().order_by('-id')
    context = {'leave':leave_request}
    return render(request, 'hod/staff_leave_request.html',context) 

def staff_leave_request_approve(request,id):
    leave = StaffLeave.objects.get(id=id) 
    leave.status = 1
    leave.save() 
    return redirect('staff_leave_request') 

def staff_leave_request_disapprove(request,id):
    leave = StaffLeave.objects.get(id=id) 
    leave.status = 2
    leave.save() 
    return redirect('staff_leave_request') 


def staff_feedback(request):
    stf_feedback = Feedback.objects.all()
    if request.method == 'POST':
        feedback_id = request.POST.get('feedback_id')
        reply_msg = request.POST.get('reply_msg')
        
        feedback = Feedback.objects.get(id=feedback_id)   
        print(feedback) 
        feedback.replyback_msg = reply_msg
        feedback.save() 
        messages.success(request,'Successfully Sent') 
        return redirect('staff_feedback') 
        
    context = {'staff_feedback':stf_feedback} 
    return render(request,'hod/staff_feedback.html',context)  

def student_notification(request):
    student= Student.objects.all() 
    notification_list = StudentNotification.objects.all() 
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        msg = request.POST.get('msg')
        
        student = Student.objects.get(user=student_id) 
        student_notifications = StudentNotification(
            student = student,
            message = msg,

        )
        student_notifications.save() 
        messages.success(request,'Send Notificaion Successfully!') 
        return redirect('student_notification') 


    context = {
        'students': student,
        'notification_list':notification_list,
    } 
    return render(request, 'hod/student_notification.html',context) 


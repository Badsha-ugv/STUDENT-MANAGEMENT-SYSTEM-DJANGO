
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views,hod_views,student_views,staff_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base,name='base'),
    #login
    path('',views.login_user,name='login'),
    path('userLogin/',views.userLogin,name='userLogin'),
    #logout
    path('logout/',views.userLogout,name='logout'),

    #HOD
    path('hod/home/',hod_views.home,name='hod_home'),
        #STUDENT
    path('hod/add_student/',hod_views.add_student,name='add_student'),
    path('hod/view_student/',hod_views.view_student,name='view_student'),
    path('hod/edit_student/<str:id>/',hod_views.edit_student,name='edit_student'),
    path('hod/delete_student/<str:id>/',hod_views.delete_student,name='delete_student'),
        #COURSE
    path('hod/add_course/',hod_views.add_course,name='add_course'),
    path('hod/view_course/',hod_views.view_course,name='view_course'),
    path('hod/update_course/<str:id>/',hod_views.update_course,name='update_course'),
    path('hod/delete_course/<str:id>/',hod_views.delete_course,name='delete_course'),

        #STAFF
    path('hod/add_staff/',hod_views.add_staff,name='add_staff'),
    path('hod/view_staff/',hod_views.view_staff,name='view_staff'),
    path('hod/update_staff/<str:id>/',hod_views.update_staff,name='update_staff'),
    path('hod/delete_staff/<str:id>/',hod_views.delete_staff,name='delete_staff'),
        #SUBJECT
    path('hod/add_subject/',hod_views.add_subject,name='add_subject'),
    path('hod/view_subject/',hod_views.view_subject,name='view_subject'),
    path('hod/edit_subject/<str:id>/',hod_views.edit_subject,name='edit_subject'),
    path('hod/delete_subject/<str:id>/',hod_views.delete_subject,name='delete_subject'),
        #SESSION YEAR
    path('hod/add_session/',hod_views.add_session,name='add_session'),
    path('hod/view_session/',hod_views.view_session,name='view_session'),
    path('hod/update_session/<str:id>/',hod_views.update_session,name='update_session'),
    path('hod/delete_session/<str:id>/',hod_views.delete_session,name='delete_session'),
        #NOTIFICATION 
    path('hod/send_staff_notification/',hod_views.send_staff_notification,name='send_staff_notification'),
    
    path('hod/send_student_notification/',hod_views.send_student_notification,name='send_student_notification'),

     path('hod/save_student_notification/',hod_views.save_student_notification,name='save_student_notification'),
        #LEAVE-STAFF
    path('hod/staff_leave_request/',hod_views.staff_leave_request,name = 'staff_leave_request'),
    path('hod/staff_leave_request/approve_btn/<str:id>/',hod_views.staff_leave_request_approve,name = 'staff_leave_request_approve'),
    path('hod/staff-leave-request/disapprove_btn/<str:id>/',hod_views.staff_leave_request_disapprove,name = 'staff_leave_request_disapprove'),
    
        #LEAVE STUDENT 
    path('hod/leave_student_hod',hod_views.leave_student_hod,name='leave_student_hod'),
    path('hod/student_leave_request_approve/<str:id>/',hod_views.student_leave_request_approve,name='student_leave_request_approve'),
    path('hod/student_leave_request_disapprove/<str:id>/',hod_views.student_leave_request_disapprove,name='student_leave_request_disapprove'),

    
        #FEEDBACK
    path('hod/staff_feedback/',hod_views.staff_feedback,name='staff_feedback'),
    path('hod/student_feedback_hod/',hod_views.student_feedback_hod,name='student_feedback_hod'),
        #ATTENDANCE 
    path('hod/view_all_attendance/',hod_views.view_all_attendance,name='view_all_attendance'),
    
    

    
    #STAFF - SECTION
    path('staff/',staff_views.staff_home,name='staff_home'),
    
    path('staff/staff_notification/',staff_views.staff_notification,name='staff_notification'),
    path('staff/seen_staff_notification/<str:id>/',staff_views.seen_staff_notification,name='seen_staff_notification'),

    path('staff/staff_leave/',staff_views.staff_leave,name='staff_leave'),
    path('staff/staff_leave_save/',staff_views.staff_leave_save,name='staff_leave_save'),

    path('staff/send_feedback/',staff_views.send_feedback,name='send_feedback'),
    path('staff/save_feedback_msg/',staff_views.save_feedback_msg,name='save_feedback_msg'),

    path('staff/take_attendance/',staff_views.take_attendance,name='take_attendance'),
    path('staff/save_attendance/',staff_views.save_attendance,name='save_attendance'),

    path('staff/view_attendance/',staff_views.view_attendance,name='view_attendance'),

    # Add Student Result
    path('staff/add_result/',staff_views.add_result,name='add_result'),
    #Save Student Result
    path('staff/save_student_result/',staff_views.save_student_result,name='save_student_result'),
    #STUDENT 
    path('student/',student_views.home,name='student_home'),
    path('student/student_notification/',student_views.student_notification,name='student_notification'),

    path('student/seen_student_notification/<str:id>/',student_views.seen_student_notification,name='seen_student_notification'),
    path('student/student_feedback/',student_views.student_feedback,name='student_feedback'),
    path('student/send_student_feedback/',student_views.send_student_feedback,name='send_student_feedback'),
    
    path('student/student_leave/',student_views.student_leave,name='student_leave'),
    path('student/student_leave_save/',student_views.student_leave_save,name='student_leave_save'),

    path('student/view_attendance_student/',student_views.view_attendance_student,name='view_attendance_student'),

    path('student/view_result/',student_views.view_result,name='view_result'),
    #profile_update
    path('update_profile/',views.update_profile,name='update_profile'),
    path('profile_update_form/',views.profile_update_form,name='profile_update_form'),


]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


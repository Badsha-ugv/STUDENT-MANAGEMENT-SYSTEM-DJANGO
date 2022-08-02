
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
    path('hod/staff_notification/',hod_views.notification,name='staff_notification'),
    path('hod/student_notification/',hod_views.student_notification,name='student_notification'),


        #LEAVE-STAFF
    path('hod/staff_leave_request/',hod_views.staff_leave_request,name = 'staff_leave_request'),
    path('hod/staff_leave_request/approve_btn/<str:id>/',hod_views.staff_leave_request_approve,name = 'staff_leave_request_approve'),
    
    path('hod/staff-leave-request/disapprove_btn/<str:id>/',hod_views.staff_leave_request_disapprove,name = 'staff_leave_request_disapprove'),
        #FEEDBACK
    path('hod/staff_feedback/',hod_views.staff_feedback,name='staff_feedback'),


    #STAFF - SECTION
    path('staff/',staff_views.staff_home,name='staff_home'),
    path('staff/notification',staff_views.notification,name='notification'),
    path('staff/notificatoin/msg_seen/<str:id>/',staff_views.msg_seen,name='msg_seen'),

    path('staff/staff_leave/',staff_views.staff_leave,name='staff_leave'),
    path('staff/staff_leave_save/',staff_views.staff_leave_save,name='staff_leave_save'),

    path('staff/send_feedback/',staff_views.send_feedback,name='send_feedback'),
    path('staff/save_feedback_msg/',staff_views.save_feedback_msg,name='save_feedback_msg'),

    #STUDENT 
    path('student/',student_views.home,name='student_home'),
    path('student/see_notification/',student_views.see_notification,name='see_notification'),

    #profile_update
    path('update_profile/',views.update_profile,name='update_profile'),
    path('profile_update_form/',views.profile_update_form,name='profile_update_form'),


]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


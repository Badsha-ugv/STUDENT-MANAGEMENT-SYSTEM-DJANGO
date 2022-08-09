from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Course,SessionYear,Student,Staff,Subject,Notification,StaffLeave,Feedback,StudentNotification,StudentFeedback,StudentLeave,TakeAttendance,AttendanceReport,StudentResult
# Register your models here.

class UserModel(UserAdmin):
    list_display =  ['username','user_type']

admin.site.register(CustomUser,UserModel)

admin.site.register(Course)
admin.site.register(SessionYear)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Notification)
admin.site.register(StaffLeave) 
admin.site.register(Feedback) 
admin.site.register(StudentNotification) 
admin.site.register(StudentFeedback) 
admin.site.register(StudentLeave) 
admin.site.register(TakeAttendance) 
admin.site.register(AttendanceReport) 
admin.site.register(StudentResult) 
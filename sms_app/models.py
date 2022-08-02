from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user_type = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT'),
    )
    user_type = models.CharField(max_length=50,choices=user_type,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic',null=True,blank=True)
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class SessionYear(models.Model):
    start_date = models.CharField(max_length=100,blank=True,null=True)
    end_date = models.CharField(max_length=100,blank=True,null=True) 

    def __str__(self):
        return self.start_date + ' to '+self.end_date


class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    course_name = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    session_year = models.ForeignKey(SessionYear,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.TextField()

    def __str__(self):
        return self.user.first_name + ' '+self.user.last_name
    

class Staff(models.Model):
    user = models.OneToOneField(CustomUser,on_delete = models.CASCADE) 
    address = models.TextField()
    gender = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Subject(models.Model):
    name = models.CharField(max_length=200) 
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE) 
    course = models.ForeignKey(Course,on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True) 

    def __str__(self):
        return self.name 

class Notification(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    message = models.TextField() 
    status = models.IntegerField(null=True,default=0) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self): 
        return self.staff.user.username 

class StudentNotification(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    message = models.TextField() 
    status = models.IntegerField(null=True,default=0) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self): 
        return self.student.user.username 

class StaffLeave(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=100) 
    message = models.TextField() 
    status = models.IntegerField(null=True,default=0 )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.staff.user.first_name + " "+ self.staff.user.last_name 

class Feedback(models.Model):
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE) 
    feedback_msg = models.TextField()
    replyback_msg = models.TextField(null=True,blank=True)  
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.staff.user.first_name + " "+self.staff.user.last_name 
        
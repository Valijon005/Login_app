from django import forms
from django.db.models import fields
from .models import *


class MentorRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Mentor
        fields = ['fullname', 'age', 'gender', 'email', 'phone', 'spes']



class CourseRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Course
        fields = ['name', 'spes', 'mentor', 'student_qty', 'start', 'finish', 'price', 'status']


class StudentRegistrationForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['fullname', 'age', 'gender', 'email', 'phone', 'course', 'payment']


class LessonRegistrationForm(forms.ModelForm):
    
    class Meta:
        model = Lesson
        fields = ['data', 'time', 'room', 'course', 'student_qty', 'mentor', 'theme', 'status']
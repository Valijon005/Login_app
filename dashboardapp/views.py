from django.core import paginator
from django.shortcuts import render, redirect

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *
from .forms import *

def base(request):
    return render(request, "dashboardapp/base.html")

def students_table(request):
    # page = request.GET.get('page')
    students = Student.objects.all()[::-1]
    courses = Course.objects.all()

    if request.method == 'POST' and request.POST.get('course_id'):
        students = Student.objects.filter(course=request.POST.get('course_id'))
    else:
        students = Student.objects.all()

    # paginator = Paginator(students, 2)

    # try:
    #     students = paginator.page(page)
    # except PageNotAnInteger:
    #     students = paginator.page(1)
    # except EmptyPage:
    #     students = paginator.page(paginator.num_pages)

    context = {
        'students': students,
        'courses': courses,
    }
    return render(request, "dashboardapp/students_table.html", context)


def groups_table(request):
    courses = Course.objects.all()[::-1]
    mentors = Mentor.objects.all()
    # payment_sum = courses.student_qty * courses.price
    if request.method == 'POST' and request.POST.get('mentor_id'):
        courses = Course.objects.filter(mentor=request.POST.get('mentor_id'))
    else:
        courses = Course.objects.all()
    context = {
        'courses': courses,
        'mentors': mentors,
        # 'payment_sum': payment_sum,
    }
    return render(request, "dashboardapp/groups_table.html", context)


def lessons_table(request):
    lessons = Lesson.objects.all()[::-1]
    mentors = Mentor.objects.all()
    courses = Course.objects.all()

    if request.method == 'POST' and request.POST.get('mentor_id'):
        lessons = Lesson.objects.filter(mentor=request.POST.get('mentor_id'))
    elif request.method == 'POST' and request.POST.get('course_id'):
        lessons = Lesson.objects.filter(course=request.POST.get('course_id'))
    else:
        lessons = Lesson.objects.all()
    context = {
        'lessons': lessons,
        'mentors': mentors,
        'courses' : courses,
    }
    return render(request, "dashboardapp/lessons_table.html", context)


def dashboard(request):
    students = Student.objects.all()
    lessons = Lesson.objects.all()
    courses = Course.objects.all()
    mentors = Mentor.objects.all()
    student_qty = students.count()
    courses_qty = courses.count()
    lessons_qty = lessons.count()
    if request.method == 'POST' and request.POST.get('course_id'):
        students = Student.objects.filter(course=request.POST.get('course_id'))
    else:
        students = Student.objects.all()

    if request.method == 'POST' and request.POST.get('mentor_id'):
        courses = Course.objects.filter(mentor=request.POST.get('mentor_id'))
    else:
        courses = Course.objects.all()

    if request.method == 'POST' and request.POST.get('mentor_id'):
        lessons = Lesson.objects.filter(mentor=request.POST.get('mentor_id'))
    else:
        lessons = Lesson.objects.all()

    context = {
        'students': students,
        'lessons': lessons,
        'courses': courses,
        'mentors': mentors,
        'student_qty' : student_qty, 
        'courses_qty' : courses_qty,
        'lessons_qty' : lessons_qty
    }
    return render(request, "dashboardapp/index.html", context)

def add_course(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CourseRegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('dashboard')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CourseRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'dashboardapp/add_course.html', context)

def add_mentor(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MentorRegistrationForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('dashboard')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MentorRegistrationForm()

    context = {
        'form': form
    }

    return render(request, "dashboardapp/add_mentor.html", context)

def add_student(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = StudentRegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('dashboard')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StudentRegistrationForm()

    return render(request, "dashboardapp/add_student.html", {'form': form})

def add_lesson(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LessonRegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('dashboard')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LessonRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'dashboardapp/add_lesson.html', context)
from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('base', views.base, name="base"),
    path('add_student', views.add_student, name="add_student"),
    path('add_course', views.add_course, name="add_course"),
    path('add_mentor', views.add_mentor, name="add_mentor"),
    path('add_lesson', views.add_lesson, name="add_lesson"),
    path('students_table', views.students_table, name="students_table"),
    path('groups_table', views.groups_table, name="groups_table"),
    path('lessons_table', views.lessons_table, name="lessons_table"),

]
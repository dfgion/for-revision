from django.contrib import admin

from .models import Student, Teacher
from 

class InlineTeachers(admin.TabularInline):
    model = student_teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    list_filter = ['group']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_filter = ['subject']

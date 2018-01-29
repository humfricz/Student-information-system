from django.contrib import admin

from .models import Student,user,Document,Courses,StudentMarks
admin.site.register(Student)
admin.site.register(user)
admin.site.register(Courses)
admin.site.register(StudentMarks)
from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Student,User,Document,Courses,StudentMarks,Dictionary

# Register your models here.
class StudentMarksAdmin(admin.ModelAdmin):
    search_fields = ['SID']

# class MyAdminSite(AdminSite):
#     site_header = 'Faculty SIS'


admin.site.register(User)
admin.site.register(Dictionary)
admin.site.register(Student)
admin.site.register(Courses)
# admin2 = MyAdminSite()
admin.site.register(StudentMarks,StudentMarksAdmin)
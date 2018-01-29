from django.conf.urls import url
from . import views
from sis.views import *
from django.contrib import admin
urlpatterns = [
url(r'^$', views.index, name = 'index'),
url(r'^home', views.login, name= 'login'),
url(r'^studentlogin', views.studentlogin, name= 'studentlogin'),
url(r'^changepassword', views.changepassword, name= 'changepassword'),
url(r'^Gradingsystem', views.Gradingsystem, name= 'Gradingsystem'),
url(r'^logout/$', logout_page),
url(r'^list/$', views.list, name='list'),
url(r'^courseList/$', views.courseList, name='courseList'),
url(r'^studentMarkslist/$', views.studentMarkslist, name='studentMarkslist'),
url(r'^studentInfo/$', views.studentInfo, name='studentInfo'),
url(r'^batchInfo/$', views.batchInfo, name = 'batchInfo'),
url(r'^markssheet/$', views.markssheet, name = 'markssheet'),
url(r'^Transcript/$', views.Transcript, name = 'Transcript'),
url(r'^bulkTranscript', views.bulkTranscript, name = 'bulkTranscript'),
url(r'^help', views.help, name = 'help'),
]
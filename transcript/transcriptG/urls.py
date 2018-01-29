from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^validate/',views.validate,name='validate'),
    url(r'^register/$',views.register,name='register'),
    url(r'^homevalidate/',views.homevalidate,name='homevalidate'),
    url(r'^courseList/$', views.courseList, name='courseList'),
    url(r'^studentMarkslist/$', views.studentMarkslist, name='studentMarkslist'),
    url(r'^list/$', views.list, name='list'),
    url(r'^Uploadd/$', views.Uploadd, name='Uploadd'),
    url(r'^TranscriptGen/$', views.TranscriptGen, name='TranscriptGen'),
    url(r'^calculateGPA/$', views.calculateGPA, name='calculateGPA'),
]


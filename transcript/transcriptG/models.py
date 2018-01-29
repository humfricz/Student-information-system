from django.db import models

# Create your models here

# Creating Document Model
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

# Creating Student Model
class Student(models.Model):
	SID = models.CharField(max_length = 12)
	firstname = models.CharField(max_length = 30)
	lastname = models.CharField(max_length = 30)
	emailid = models.EmailField(max_length = 400)
	phnum = models.CharField(max_length = 15)
	yearofjoining = models.IntegerField(default = 0)
	yearofpassing = models.IntegerField(default = 0)
	batchNo = models.IntegerField(default = 0)
	def __unicode__(self):              
		return self.firstname+ " "+ self.lastname

# Creating User Model

class user(models.Model):
	Fname = models.CharField(max_length=20)
	Lname = models.CharField(max_length=20)
	Email = models.EmailField(max_length=50)
	password= models.CharField(max_length=30)
	userType = models.CharField(max_length=25)
	def __unicode__(self):              
		return self.Fname+" "+self.Lname

# Creating Course Model

class Courses(models.Model):
	CID = models.CharField(max_length = 10)
	CName = models.CharField(max_length = 50)
	year = models.IntegerField(default = 0)
	term = models.IntegerField(default = 0)
	credits = models.IntegerField(default = 0)
	Courseyear = models.IntegerField(default = 0)
	def __unicode__(self):             
		return self.CName

# Creating StudentMarks Model

class StudentMarks(models.Model):
	SID = models.CharField(max_length=12)
	CID = models.CharField(max_length=10)
	grade = models.CharField(max_length=2)
	description = models.CharField(default="null",max_length=50)
	def __unicode__(self):              
		return self.SID
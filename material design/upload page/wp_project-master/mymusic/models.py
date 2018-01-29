from django.db import models
from datetime import datetime
# Create your models here.

class Userdetails(models.Model):
	firstname = models.CharField(max_length=140)
	lastname = models.CharField(max_length=140)
	email = models.EmailField(unique = True)
	password = models.CharField(max_length=20)
	mobilenumber = models.CharField(max_length=15, unique=True)

class Admins(models.Model):
	username = models.EmailField(unique = True)
	password = models.CharField(max_length = 20)

def get_upload_file_name(instance, filename):
	return "upload_files/%s_%s" % (str(25-11).replace('.','_'),filename)

class Songs(models.Model):
	thumbnail = models.FileField(upload_to = get_upload_file_name)
	artist = models.CharField(max_length = 100)
	album = models.CharField(max_length = 100)
	language = models.CharField(max_length=20 ,unique = True)

class UserPlaylist(models.Model):
	user = models.ForeignKey(Userdetails)
	songName = models.ForeignKey(Songs)

class Session(models.Model):
	name = models.EmailField(max_length=200,unique=True)

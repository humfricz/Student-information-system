from django import forms
from models import Userdetails, Admins, Songs

class UserDetailsForm(forms.ModelForm):
	class Meta:
		model = Userdetails
		fields = ('firstname', 'lastname', 'email', 'password', 'mobilenumber')

class Adminsform(forms.ModelForm):
	class Meta:
		model = Admins
		fields = ('username', 'password')

class SongsForm(forms.ModelForm):
	class Meta:
		model = Songs
		fields = ('thumbnail','artist', 'album','language')
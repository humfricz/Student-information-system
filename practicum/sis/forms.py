from django import forms
#Students List Form
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
# Courses List Form
class CourseForm(forms.Form):
    coursefile = forms.FileField(
        label='Select a file'
    )
#Student Marks List Form
class StudentForm(forms.Form):
    studmarksfile = forms.FileField(
        label='Select a file'
    )
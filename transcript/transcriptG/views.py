
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import user,Student
import cgi
import os
import json
import calendar
from django.utils import timezone
from django.conf import settings
from django.template import RequestContext, loader
import reportlab  
from reportlab.pdfbase import pdfmetrics  
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer  
from reportlab.lib.styles import getSampleStyleSheet  
from reportlab.rl_config import defaultPageSize
from django.core.urlresolvers import reverse
from reportlab.pdfgen import canvas
from datetime import datetime
from io import BytesIO

from .models import Document,Courses,StudentMarks
from .forms import DocumentForm,CourseForm,StudentForm
# render to Login page
def index(request):
    return render(request, 'transcriptG/index.html')

# render to registration page
def register(request):
	return render(request,'transcriptG/register.html')

def Uploadd(request):
    return render(request,'transcriptG/upload.html')

#validating the registration Fields
def validate(request):
    # return HttpResponse("ssucess")
    First_name = request.GET.get('First_name')
    Last_name = request.GET.get('Last_name')
    EmailId = request.GET.get('EmailId')
    password1 = request.GET.get('password1')
    userType = request.GET.get('userType')
    response = {}
    if not user.objects.filter(Email=EmailId):
        s = user(Fname=First_name,Lname = Last_name, Email = EmailId,password= password1,userType=userType)
        s.save()
        return render_to_response(
               './transcriptG/index.html',
               context_instance=RequestContext(request)
           )
    else:
        return HttpResponse("Email already exits")

def homevalidate(request):
    # return HttpResponse('deepakkkk here')
    userid = request.GET.get('email')
    paswd = request.GET.get('password')
    
    if user.objects.filter(Email = userid,password=paswd,userType='admin'):
        # response
        return HttpResponse('true')
    elif user.objects.filter(Email = userid,password=paswd,userType='user'):
        return HttpResponse('false')
    else:
        return HttpResponse('none')

# validating and storing the data of uploaded student details csv file
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            docfile = request.FILES['docfile']
            for row in docfile:
                student = Student()
                row = row.split(",")
                student.SID = row[0]
                student.firstname = row[1]
                student.lastname = row[2]
                student.emailid = row[3]
                student.phnum = row[4]
                student.yearofjoining = row[5]
                student.yearofpassing = row[6]
                student.batchNo = row[7]
                student.save()

            # Redirect to the document list after POST
            return render_to_response(
                'transcriptG/uploadsuccess.html',
                {'form': form},
                context_instance=RequestContext(request)
            )
            # return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    students = Student.objects.all()

    # # Render list page with the documents and the form
    # return HttpResponse('Fialure in uploading the student details')
    return render_to_response(
        'transcriptG/DocUpload.html',
        {'documents': students, 'form': form},
        context_instance=RequestContext(request)
    )

# validating and storing the data of uploaded couerses list csv file
def courseList(request):
    # Handle file upload
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            coursefile = request.FILES['coursefile']
            for row in coursefile:
                course = Courses()
                row = row.split(",")
                course.CID = row[0]
                course.CName = row[1]
                course.year = row[2]
                course.term = row[3]
                course.credits = row[4]
                course.save()

            # Redirect to the document list after POST
            return render_to_response(
                'transcriptG/uploadsuccess.html',
                {'form': form},
                context_instance=RequestContext(request)
            )
            # return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = CourseForm()  # A empty, unbound form

    # Load documents for the list page
    courses = Courses.objects.all()

    # # Render list page with the documents and the form
    # return HttpResponse('Fialure in uploading the student details')
    return render_to_response(
        'transcriptG/CoursesUpload.html',
        {'documents': courses, 'form': form},
        context_instance=RequestContext(request)
    )

# validating and storing the data of uploaded student marks list csv file
def studentMarkslist(request):
    # Handle file upload
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            studmarksfile = request.FILES['studmarksfile']
            for row in studmarksfile:
                studmarks = StudentMarks()
                row = row.split(",")
                studmarks.SID = row[0]
                studmarks.CID = row[1]
                studmarks.grade = row[2]
                studmarks.description = row[3]
                studmarks.save()

            # Redirect to the document list after POST
            return render_to_response(
                'transcriptG/uploadsuccess.html',
                {'form': form},
                context_instance=RequestContext(request)
            )
            # return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = StudentForm()  # A empty, unbound form

    # Load documents for the list page
    studmarkslist = StudentMarks.objects.all()

    # # Render list page with the documents and the form
    # return HttpResponse('Fialure in uploading the student details')
    return render_to_response(
        'transcriptG/StudentMarksUpload.html',
        {'documents': studmarkslist, 'form': form},
        context_instance=RequestContext(request)
    )

def TranscriptGen(request):
    return render(request,'transcriptG/generateTranscript.html')

def handle_exception(e):
    print(e)
    print('But I can be safe!')

def calculateGPA(request):
    from reportlab.lib import colors  
    from reportlab.lib.units import inch
    # Create the HttpResponse object with the appropriate PDF headers.
    stud_id = request.GET.get('stud_id')
    filename = stud_id
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename={0}.pdf'.format(filename)
    buffer=BytesIO()
    # p= canvas.Canvas("filename.pdf")
    
    p = canvas.Canvas(buffer)
    # Create the PDF object, using the response object as its "file."

   
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    students_ids=Student.objects.all()
    count = 0
    today = datetime.now()
    for st in students_ids:
        if stud_id in st.SID:
            count = count + 1
    if count > 0:
        stud_details = Student.objects.filter(SID = stud_id)
        p.setFont('Times-Bold',7)
        p.drawString(20,690,"MSIT")
        p.drawString(20,680, str(stud_details[0].yearofjoining)+"-"+str(stud_details[0].yearofpassing))
        p.drawString(20,670,"Date Of Issue:")
        p.drawString(20,660,today.strftime("%d-%B-%Y"))
        p.setFont('Times-Bold',7)
        p.drawString(20,650,"Consolidated Mark Sheet")
        p.setFont('Times-Bold',11)
        p.drawString(115,690,"Name:" )
        p.setFont('Times-Bold',12)
        p.drawString(149,690,stud_details[0].firstname+" "+stud_details[0].lastname)
        p.setFont('Times-Roman',10)
        p.drawString(465,690,"Roll No: ")
        p.setFont('Times-Bold',10)
        p.drawString(501, 690, stud_details[0].SID)
        p.setFont('Times-BoldItalic',11)
        p.drawString(115,670,"MASTER OF SCIENCE IN INFORMATION TECHNOLOGY")
        p.setFont('Times-Roman',10)
        p.drawString(115,650,"CGPA:")
        p.drawString(115,630,"Credits Obtained:")
        p.drawString(445,640,"PercentageRange:")
        p.drawString(395,630,"Required Credits for Completion:")
        p.setFont('Times-Bold',9)
        p.drawString(115, 600, "Code")
        p.drawString(235, 600, "Course Name")
        p.drawString(435, 600, "Grade")
        p.drawString(485, 600, "Credits")
        p.drawString(115, 580,"First Year")
        p.setFont('Times-Roman',9)
        gradeDictionary={'EX':10.0,'A+':9.5,'A':9.0,'B+':8.5,'B':8.0,'B-':7.5,'C':7.0,'Ex':10.0,'A-':9.0}

        grade_details= StudentMarks.objects.filter(SID = stud_details[0].SID)
        GPA = 0
        CGPA = 0
        sum_of_credits = 0
        temp = 0
        for j in grade_details:
            if j.grade == 'F':
                sum_of_credits = 0
                return HttpResponse('student has a F grade')

            grade = gradeDictionary[j.grade]
            
            credits_details = Courses.objects.filter(CID=j.CID)

            credits = credits_details[0].credits
            
            sum_of_credits = sum_of_credits + credits
            GPA = GPA + (grade*credits)

            if credits_details[0].year == 1 and 'SS' not in credits_details[0].CID :
                p.drawString(445, (560-temp), j.grade)
                p.drawString(115, (560-temp), credits_details[0].CID)
                p.drawString(170, (560-temp), credits_details[0].CName)
                p.drawString(505, (560-temp), str(credits))
                # p.drawString(460, 650, str(credits))
                temp = temp + 15

        p.setFont('Times-Bold',9)
        p.drawString(115,(560-temp),"Second Year")
        p.setFont('Times-Roman',9)
        temp = temp + 15
        for j in grade_details:
            if j.grade == 'F':
                sum_of_credits = 0
                return HttpResponse('student has a F grade')

            grade = gradeDictionary[j.grade]
            
            credits_details = Courses.objects.filter(CID=j.CID)

            credits = credits_details[0].credits

            if credits_details[0].year == 2 and 'SS' not in credits_details[0].CID :
                p.drawString(445, (560-temp), j.grade)
                p.drawString(115, (560-temp), credits_details[0].CID)
                p.drawString(170, (560-temp), credits_details[0].CName)
                p.drawString(505, (560-temp), str(credits))
                # p.drawString(460, 650, str(credits))
                temp = temp + 15


        p.drawString(190, 630, str(sum_of_credits))
        p.drawString(530, 630, str(sum_of_credits))
        if not sum_of_credits == 0:
            CGPA = GPA/sum_of_credits
            p.drawString(150,650,str(round(CGPA,1)))
        
        # canvas.drawCentredString(2.75*inch, 2.5*inch, "Font size examples")
        if CGPA == 10.0 :
            p.drawString(520,640,"96-100") 
        if CGPA >= 9.0 and CGPA <10.0:
            p.drawString(520,640,"91-95")
        if CGPA >= 8.0 and CGPA < 9.0:
            p.drawString(520,640,"86-90")
        if CGPA >= 7.0 and CGPA < 8.0:
            p.drawString(520,640,"81-85")
        if CGPA >= 6.0 and CGPA < 7.0:
            p.drawString(520,640,"76-80")
        if CGPA >= 5.0 and CGPA < 6.0:
            p.drawString(520,640,"70-75")
        if CGPA < 5.0:
            p.drawString(520,640,"<70")

        temp = temp+80
        p.setFont('Times-Bold',10)
        p.drawString(400,560-temp,"Coordinator MSIT Division")

        temp = temp + 140
        p.setFont('Times-Italic',9)
        p.drawString(115,70,"CGPA: Cumulative Grade Point Average")
        temp = temp + 15
        p.drawString(115,50,"EX = 10.0; A+ = 9.5; A = 9.0; B+ = 8.5; B = 8.0; C = 7.0")

        p.showPage()

        stud_details = Student.objects.filter(SID = stud_id)
        p.setFont('Times-Bold',7)
        p.drawString(20,690,"MSIT")
        p.drawString(20,680, str(stud_details[0].yearofjoining)+"-"+str(stud_details[0].yearofpassing))
        p.drawString(20,670,"Date Of Issue:")
        p.drawString(20,660,today.strftime("%d-%B-%Y"))
        p.setFont('Times-Bold',7)
        p.drawString(20,650,"Consolidated Marks Sheet")
        p.setFont('Times-Bold',11)
        p.drawString(115,690,"Name:" )
        p.setFont('Times-Bold',12)
        p.drawString(149,690,stud_details[0].firstname+" "+stud_details[0].lastname)
        p.setFont('Times-Roman',10)
        p.drawString(465,690,"Roll No: ")
        p.setFont('Times-Bold',10)
        p.drawString(501, 690, stud_details[0].SID)
        p.setFont('Times-BoldItalic',11)
        p.drawString(115,670,"MASTER OF SCIENCE IN INFORMATION TECHNOLOGY")
        p.setFont('Times-Roman',10)
        p.drawString(115,650,"CGPA:")
        p.drawString(115,630,"Credits Obtained:")
        p.drawString(445,640,"PercentageRange:")
        p.drawString(395,630,"Required Credits for Completion:")
        p.setFont('Times-Bold',9)
        p.drawString(115, 600, "Code")
        p.drawString(235, 600, "Course Name")
        p.drawString(435, 600, "Grade")
        p.drawString(485, 600, "Credits")
        gradeDictionary={'EX':10.0,'A+':9.5,'A':9.0,'B+':8.5,'B':8.0,'B-':7.5,'C':7.0,'Ex':10.0,'A-':9.0}
        p.drawString(115, 580, "Soft Skills")
        p.setFont('Times-Roman',9)


        grade_details= StudentMarks.objects.filter(SID = stud_details[0].SID)
        temp = 0
        for j in grade_details:
            if j.grade == 'F':
                sum_of_credits = 0
                return HttpResponse('student has a F grade')

            grade = gradeDictionary[j.grade]
            
            credits_details = Courses.objects.filter(CID=j.CID)

            credits = credits_details[0].credits

            if 'SS' in credits_details[0].CID :
                p.drawString(445, (560-temp), j.grade)
                p.drawString(115, (560-temp), credits_details[0].CID)
                p.drawString(170, (560-temp), credits_details[0].CName)
                p.drawString(505, (560-temp), str(credits))
                # p.drawString(460, 650, str(credits))
                temp = temp + 15

        p.setFont('Times-Roman',9)
        p.drawString(190, 630, str(sum_of_credits))
        p.drawString(530, 630, str(sum_of_credits))
        if not sum_of_credits == 0:
            CGPA = GPA/sum_of_credits
            p.drawString(150,650,str(round(CGPA,1)))
        
        # canvas.drawCentredString(2.75*inch, 2.5*inch, "Font size examples")
        if CGPA == 10.0 :
            p.drawString(520,640,"96-100") 
        if CGPA >= 9.0 and CGPA <10.0:
            p.drawString(520,640,"91-95")
        if CGPA >= 8.0 and CGPA < 9.0:
            p.drawString(520,640,"86-90")
        if CGPA >= 7.0 and CGPA < 8.0:
            p.drawString(520,640,"81-85")
        if CGPA >= 6.0 and CGPA < 7.0:
            p.drawString(520,640,"76-80")
        if CGPA >= 5.0 and CGPA < 6.0:
            p.drawString(520,640,"70-75")
        if CGPA < 5.0:
            p.drawString(520,640,"<70")


        temp = temp+80
        p.setFont('Times-Bold',11)
        p.drawString(400,560-temp,"Coordinator MSIT Division")

        temp = temp + 250
        p.setFont('Times-Italic',9)
        p.drawString(115,70,"CGPA: Cumulative Grade Point Average")
        temp = temp + 15
        p.drawString(115,50,"EX = 10.0; A+ = 9.5; A = 9.0; B+ = 8.5; B = 8.0; C = 7.0")

        p.showPage()
        p.save()
        pdf= buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
    else:
        return HttpResponse("Student id not found")
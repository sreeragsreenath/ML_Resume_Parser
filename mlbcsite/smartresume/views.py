from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import PyPDF2


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def index2(request):
	return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.

def index(request):
	context = {'lol': 'latest_question_list'}
	return render(request, 'index.html', context)

def about(request):
	context = {'lol': 'latest_question_list'}
	return render(request, 'about.html', context)

def upload_file(request):
	context = {'lol': 'latest_question_list'}
	if request.method == 'POST':
		myfile = request.FILES['file']
		print(myfile)
		pdfFileObj = myfile
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		pdfReader.numPages
		pageObj = pdfReader.getPage(0)  
		text = pageObj.extractText()
		print(text)
		return render(request, 'upload_file.html', context)
	else:
		form = UploadFileForm()
	return render(request, 'upload_file.html', context)


    
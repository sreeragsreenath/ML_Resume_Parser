from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import PyPDF2
import nltk
from textblob import TextBlob
import pickle
from django.contrib.staticfiles.templatetags.staticfiles import static


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
	context['result'] = False
	if request.method == 'POST':
		profiles = ["Software Developer","Web Developer","Java Developer","System Administrator","Software Engineer","QA Engineer","PHP Developer","Senior Software Engineer","Programmer","IT Specialist","Web Designer","Android Developer","C++ Software Developer","Python Developers","Data Analyst"]
		myfile = request.FILES['file']
		print(myfile)
		pdfFileObj = myfile
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		pdfReader.numPages
		pageObj = pdfReader.getPage(0)  
		text = pageObj.extractText()
		print(text)
		url = "f.pkl"
		cl = pickle.load(open(url, 'rb'))
		#-----------------------------------------------
		blob = TextBlob(text)
		blob.noun_phrases
		text = ' '.join(blob.noun_phrases)
		text
		#---------------------------------------------------
		print(cl.classify(text))
		prob_dist = cl.prob_classify(text)
		rank = []
		for k in profiles:
		    ar = [k,prob_dist.prob(k)]
		    rank.append(ar)
		rank = sorted(rank, key=lambda x: x[1],reverse=True)
		print(rank)
		context['result'] = True
		context['profiles'] = rank
		return render(request, 'upload_file.html', context)
	else:
		form = UploadFileForm()
	return render(request, 'upload_file.html', context)


    
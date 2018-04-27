from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms

import PyPDF2
import pickle
import nltk
nltk.download('brown')
nltk.download('punkt')
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

profiles = ["Software Developer","Web Developer","Java Developer","System Administrator","Software Engineer","QA Engineer","PHP Developer","Senior Software Engineer","Programmer","IT Specialist","Web Designer","Android Developer","C++ Software Developer","Python Developers","Data Analyst"]

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def index2(request):
	return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.

def index(request):
	context = {'test': 'latest_question_list'}
	return render(request, 'index.html', context)

def about(request):
	context = {'test': 'latest_question_list'}
	return render(request, 'about.html', context)

# def login(request):
# 	context = {'lol': 'latest_question_list'}
# 	return render(request, 'login.html', context)

# def register(request):
# 	context = {'lol': 'latest_question_list'}
# 	return render(request, 'register.html', context)	

def upload_file(request):
	context = {'test': 'latest_question_list'}
	context['isResults'] = False
	user= request.user
	context['role'] = request.user.groups.all()[0]
	if request.method == 'POST':
		myfile = request.FILES['file']
		file = open('./smartresume/static/models/model.pkl','rb')
		cl = pickle.load(file)
		pdfFileObj = myfile
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		pdfReader.numPages
		pageObj = pdfReader.getPage(0)  
		text = pageObj.extractText()
		blob = TextBlob(text)
		blob.noun_phrases
		text = ' '.join(blob.noun_phrases)
		print(cl.classify(text))
		prob_dist = cl.prob_classify(text)
		rank = []
		for k in profiles:
			ar = [k,prob_dist.prob(k)]
			rank.append(ar)
		rank = sorted(rank, key=lambda x: x[1],reverse=True)
		rank = rank[:5]
		context['ranks'] = rank[:5]
		print(user.groups.all()[0])
		context['user'] = user
		context['isResults'] = True
		return render(request, 'upload_file.html', context)
	else:
		form = UploadFileForm()
	print(user)
	
	return render(request, 'upload_file.html', context)


def userLogin(request):
	context = {'test': 'latest_question_list'}
	print("request.user : ",request.user)
	if not request.user == "AnonymousUser":
		context['message'] = ''
		if request.method == 'POST':
			print("Im in")
			username = request.POST.get('inputEmail')
			password = request.POST.get('inputPassword')
			print("username :",username,"password : ",password)
			user = authenticate(request, username=username, password=password)
			# grp = request.user.groups.values_list('name',flat=True)
			# print("user : ",user,"user.group :",user.groups.all()[0])
			print("username :",user.groups.all())
			context['user'] = user
			context['role'] = user.groups.all()[0]
			if user is not None:
				login(request, user)
				return redirect('upload_file')
			else:
				context['message'] = 'Username or Password not correct'
				render(request, 'userLogin.html', context)
				# messages.error(request,'username or password not correct')

		return render(request, 'userLogin.html', context)
	else:
		return redirect('userLogin')

def register(request):
	context = {'test': 'latest_question_list'}
	if request.method == 'POST':
		print("Im in")
		username = request.POST.get('inputEmail')
		password = request.POST.get('inputPassword')
		emailId = request.POST.get('emailId')
		print("username :",username,"password : ",password)
		try:
			user = User.objects.create_user(username,emailId, password)
			print("user :",user,"  User Created")
			my_group = Group.objects.get(name='customer')
			my_group.user_set.add(user)
			print("group :",my_group,"user.group :",user.groupname,"  user added in Customer ")
			return render(request, 'userLogin.html', context)
		except:
		    context['message'] = 'UserName already exist, please enter another UserName.'

	return render(request, 'register.html', context)	

def logout_view(request):
	# context = {'lol': 'latest_question_list'}
	# logout(request)
	
	# user = getattr(request, 'user', None)
 #    if hasattr(user, 'is_authenticated') and not user.is_authenticated():
 #        user = None
	#     user_logged_out.send(sender=user.__class__, request=request, user=user)

	request.session.flush()
	if hasattr(request, 'user'):
		request.user = AnonymousUser()
	return redirect('index')
    
# if user.groups.filter(name='groupname').exists():
#     # Action if existing

# else:
#     # Action if not existing
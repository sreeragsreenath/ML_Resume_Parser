from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
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

# def login(request):
# 	context = {'lol': 'latest_question_list'}
# 	return render(request, 'login.html', context)

# def register(request):
# 	context = {'lol': 'latest_question_list'}
# 	return render(request, 'register.html', context)	

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


def userLogin(request):
	context = {'lol': 'latest_question_list'}
	context['message'] = ''
	context['existingUser'] = ''
	if request.method == 'POST':
		print("Im in")
		username = request.POST.get('inputEmail')
		password = request.POST.get('inputPassword')
		print("username :",username,"password : ",password)
		user = authenticate(request, username=username, password=password)
		print("user : ",user)
		context = {'user': user}
		if user is not None:
			login(request, user)
			request.session['member_id'] = user.id
			return render(request, 'upload_file.html', context)
		else:
			context['message'] = 'Username or Password not correct'
			render(request, 'userLogin.html', context)
			# messages.error(request,'username or password not correct')

	return render(request, 'userLogin.html', context)

def register(request):
	context = {'lol': 'latest_question_list'}
	if request.method == 'POST':
		print("Im in")
		username = request.POST.get('inputEmail')
		password = request.POST.get('inputPassword')
		emailId = request.POST.get('emailId')
		print("username :",username,"password : ",password)
		try:
			user = User.objects.create_user(username,emailId, password)
			print("user :",user,"  User Created ")
			return render(request, 'userLogin.html', context)
		except:
		    context['message'] = 'UserName already exist, please enter another UserName.'
		# except IntegrityError as e:
		#     # handle_runtime(re)
		#     context['message'] = 'UserName already exist, please enter another UserName.'

	return render(request, 'register.html', context)	

def logout_view(request):
	context = {'lol': 'latest_question_list'}
	logout(request)
	return render(request, 'index.html', context)

    

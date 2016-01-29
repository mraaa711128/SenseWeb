from django.shortcuts import render, redirect
from django.http import HttpResponse
from SenseWeb.models import Movie, Quiz
from SenseWeb.views.forms import MovieForm, QuizForm, QuizSetFormSet, QuizAnswerFormSet

# Create your views here.

def movies(request):
	if request.method == 'GET':
		movies = Movie.objects.all()

	return render(request,'Movies.html',{'movies':movies})

def movie(request,movieid):
	movie = None
	if movieid != '0':
		movie = Movie.objects.get(id=movieid)

	if request.method == 'GET':
		if movie is None:
			form = MovieForm()
		else:
			form = MovieForm(instance=movie)
	else:
		if movie is None:
			form = MovieForm(request.POST)
		else:
			form = MovieForm(request.POST,instance=movie)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponse('')

	return render(request,'MovieDialog.html',{'form':form,'movie':movie})

def delete_movie(request,movieid):
	movie = None
	if movieid != '0':
		movie = Movie.objects.get(id=movieid)

	if request.method == 'POST':
		if movie is not None:
			movie.delete()

	return HttpResponse('')

def quizzes(request):
	if request.method == 'GET':
		quizzes = Quiz.objects.all()

	return render(request,'Quizzes.html',{'quizzes':quizzes})

def quiz(request,quizid):
	quiz = None
	if quizid != '0':
		quiz = Quiz.objects.get(id=quizid)

	if request.method == 'GET':
		if quiz is None:
			form = QuizForm()
		else:
			form = QuizForm(instance=quiz)
	else:
		if quiz is None:
			form = QuizForm(request.POST)
		else:
			form = QuizForm(request.POST,instance=quiz)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponse('')
	return render(request,'QuizDialog.html',{'form':form,'quiz':quiz})

def delete_quiz(request,quizid):
	quiz = None
	if quizid != '0':
		quiz = Quiz.objects.get(id=quizid)

	if request.method == 'POST':
		if quiz is not None:
			quiz.delete()

	return HttpResponse('')

def quizset(request,quizid):
	quiz = None
	if quizid != '0':
		quiz = Quiz.objects.get(id=quizid)

	if request.method == 'GET':
		if quiz is None:
			formset = QuizSetFormSet()
		else:
			formset = QuizSetFormSet(instance=quiz)
	else:
		if quiz is None:
			formset = QuizSetFormSet(request.POST)
		else:
			formset = QuizSetFormSet(request.POST,instance=quiz)
		if formset.is_valid():
			formset.save(commit=True)
			return HttpResponse('')
	return render(request,'QuizSetDialog.html',{'formset':formset,'quiz':quiz})

def quizanswer(request,quizid):
	quiz = None
	if quizid != '0':
		quiz = Quiz.objects.get(id=quizid)

	if request.method == 'GET':
		if quiz is None:
			formset = QuizAnswerFormSet()
		else:
			formset = QuizAnswerFormSet(instance=quiz)
	else:
		if quiz is None:
			formset = QuizAnswerFormSet(request.POST)
		else:
			formset = QuizAnswerFormSet(request.POST,instance=quiz)
		if formset.is_valid():
			formset.save(commit=True)
			return HttpResponse('')
	return render(request,'QuizAnswerDialog.html',{'formset':formset,'quiz':quiz})

def msgpage(request):
	return render(request,'SendMessage.html')


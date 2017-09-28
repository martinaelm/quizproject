from quiz.models import Quiz
from django.shortcuts import render

def startpage(request):
	context = {
		"quizzes": Quiz.objects.all(),	

	}
	return render(request, "startpage.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[quiz_number - 1],
		"quiz_number": quiz_number,
	}
	return render(request, "quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
	"question_number": question_number,
	"question": "Välj en av dessa låtar",
	"answer1": "Justin Bieber - Baby",
	"answer2": "Max Richter - The Departure",
	"answer3": "Scooter - Faster Harder Scooter",
	"quiz_number": quiz_number,

	}
	return render(request, "question.html", context)

def completed(request, quiz_number):
	context = {
		"correct": 12,
	    "total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "completed.html", context)



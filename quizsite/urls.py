"""quizsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from quiz import views

from django.contrib import admin

urlpatterns = [
	path("", views.startpage, name="start_page"),
	path("quiz/<int:quiz_number>/", views.quiz, name="quiz_page"),
	path("quiz/<int:quiz_number>/question/<int:question_number>/", views.question, name="question_page"),
	path("quiz/<int:quiz_number>/completed/", views.completed, name="completed_page"),
	path('admin/', admin.site.urls),
]
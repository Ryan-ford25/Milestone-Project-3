from django.shortcuts import render
from django.views import generic
from .models import Question
# Create your views here.

class QuestionList(generic.ListView):
    model = Question

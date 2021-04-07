from django.shortcuts import render 
from .models import Assignments

def index(request):
    assignment = Assignments.objects.all() 
    context = {'assignment': assignment} 
    return render(request, 'grading/extend.html', context)
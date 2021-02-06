from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def abstract(request):
    return render(request, 'abstract.html', {})




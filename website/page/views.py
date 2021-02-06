from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def abstarct(request):
    return render(request, 'abstarct.html', {})




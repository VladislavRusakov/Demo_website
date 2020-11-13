from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'hello/index.html') #render вызывает шаблоны страниц из темплейтс

def about(request):
    return render(request, 'hello/about.html')

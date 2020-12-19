from django.shortcuts import render

#Just so y'all know, this is where the magic happens

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})
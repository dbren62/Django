from django.shortcuts import render

# Create your views here.

def index(request):
    """ The homepage for learning log. """
    return render(request, 'MainApp/index.html')


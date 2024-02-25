# videostream/views.py
from django.shortcuts import render
from .models import Video

def home(request):
    return render(request, 'videostream/home.html')

def search(request):
    # Handle search functionality here
    return render(request, 'videostream/search.html')

def signup_view(request):
    # Your view logic here
    return render(request, 'signup.html')
def login_view(request):
    # Your view logic here
    return render(request, 'login.html')

def search(request):
    if query := request.GET.get('query'):
        # Perform search operation, for example:
        results = Video.objects.filter(title__icontains=query)
    else:
        results = []
    return render(request, 'videostream/search.html', {'results': results})

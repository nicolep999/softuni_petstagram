from django.shortcuts import render

# Create your views here.

def home_page_view(request) -> render:
    return render(request, 'common/home-page.html')
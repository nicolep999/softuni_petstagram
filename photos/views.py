from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def photo_add_view(request) -> HttpResponse:
    return render(request, 'photos/photo-add-page.html')

def photo_details_view(request) -> HttpResponse:
    return render(request, 'photos/photo-details-page.html')

def photo_edit_view(request) -> HttpResponse:
    return render(request, 'photos/photo-edit-page.html')
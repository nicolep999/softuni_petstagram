from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def pet_add_view(request) -> HttpResponse:
    return render(request, "pets/pet-add-page.html")


def pet_details_view(request, username: str, pet_slug: str) -> HttpResponse:
    return render(request, "pets/pet-details-page.html")


def pet_edit_view(request, username: str, pet_slug: str) -> HttpResponse:
    return render(request, "pets/pet-edit-page.html")


def pet_delete_view(request, username: str, pet_slug: str) -> HttpResponse:
    return render(request, "pets/pet-delete-page.html")

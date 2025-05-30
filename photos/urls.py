from photos import views
from django.urls import path, include

urlpatterns = [
    path("add/", views.photo_add_view, name="photo-add"),
    path(
        "<int:pk>/",
        include(
            [
                path("", views.photo_details_view, name="photo-details"),
                path("edit/", views.photo_edit_view, name="photo-edit"),
            ]
        ),
    ),
]

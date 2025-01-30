from django.urls import path
from . import views

urlpatterns = [
    path("", views.about_view, name="about_view"),
    path("contact", views.contact_view, name="contact_view"),
]
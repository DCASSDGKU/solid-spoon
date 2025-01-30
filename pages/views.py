from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home_view(request):
    return render(request, "pages/home.html")

def about_view(request):
    return render(request, "pages/about.html")

def contact_view(request):
    form = ContactForm
    return render(request, "pages/contact.html", {'form': form})
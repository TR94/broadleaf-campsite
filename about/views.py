from django.shortcuts import render
from .models import About, Contact


def AboutView(request, *args, **kwargs):
    # Renders the About page
    about = About.objects.all().first()
    return render(
        request,
        "about.html",
        {
            "about": about
        },
    )

def ContactView(request):
    # Renders the contact page
    contact = Contact.objects.all().first()
    return render(
        request,
        "contact.html",
        {
            "contact": contact
        },
    )
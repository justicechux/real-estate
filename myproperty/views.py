from django.shortcuts import render, redirect
from .models import services, property
from .forms import PropertyForm
from django.contrib import messages
# Create your views here.

def home_page(request):
    service = services.objects.all()
    properties = property.objects.all()
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking was successful")
    else:
        form = PropertyForm()

    context = {
        "service": service,
        "form": form,
        "properties": properties
    }
    return render(request, "myproperty/index.html", context)


def about(request):
    return render(request, "myproperty/about.html")

def service(request):
    return render(request, "myproperty/service.html")

def properties(request):
    return render(request, "myproperty/properties.html")
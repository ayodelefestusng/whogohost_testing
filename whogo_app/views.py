from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to Whogo, Ayodele!")


def contact_view(request):
    return HttpResponse("Welcome to Whogo, Contact Page!")
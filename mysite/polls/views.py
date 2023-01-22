from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def about(request):
    return render(
        request=request,
        template_name="about.html",
        context={}
    )
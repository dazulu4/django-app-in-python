from django.shortcuts import render
from .forms import RegisteredForm

# Create your views here.
def index(request):
    context = { "reg_form": RegisteredForm() }
    return render(
        request=request, 
        template_name="index.html",
        context=context)
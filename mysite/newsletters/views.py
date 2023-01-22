from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, RegisteredModelForm
from .models import Registered


# Create your views here.
def index(request):
    title = "Suscribe with us"
    if request.user.is_authenticated:
        title = f"{title} - {request.user}"
        
    form = RegisteredModelForm(request.POST or None)
    context = { 
        "reg_title": title,
        "reg_form": form 
    }
    
    if form.is_valid():
        instance = form.save(commit=False)
        name = instance.name
        if not name:
            instance.name = "Dummy Name"
        instance.save()
        
        if not name:
            # context = {"reg_title": "Gracias persona sin nombre!"
            context = {"reg_title": f"Thank you {instance.email}!"}
        else:
            context = {"reg_title": f"Thank you {instance.name}!"}
            
        # form_data = form.cleaned_data
        # model = Registered.objects.create(
        #     email=form_data.get("email"),
        #     name=form_data.get("name"))
        # print(model)
    
    if request.user.is_authenticated and request.user.is_staff:
        queryset = Registered.objects.all().order_by(
            "-timestamp").filter(name__iexact="Dummy Name")
        # .filter(email__icontains="per")
        context = {
            "queryset": queryset,
        }
    
    return render(
        request=request, 
        template_name="index.html",
        context=context)
    
    
def contact(request):
    form = ContactForm(request.POST or None)
    context={
        "contact_title": "Contact us",
        "contact_form": form,
    }
    
    if form.is_valid():
        email = form.cleaned_data.get("email")
        name = form.cleaned_data.get("name")
        message = form.cleaned_data.get("message")
        email_message = f"{name}: {message}. Sent by {email}"
        send_mail(
            subject="Contact us message",
            message=email_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER, 'dazulu4@gmail.com'],
            fail_silently=False)
        # print(email, name, message)
        # for key, value in form.cleaned_data.items():
        #     print(key, value, sep=": ")

    return render(
        request=request,
        template_name="contact.html",
        context=context)
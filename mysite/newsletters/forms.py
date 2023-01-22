from django import forms

from .models import Registered


class RegisteredModelForm(forms.ModelForm):
    class Meta:
        model = Registered
        fields = ["name", "email"]
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        _, server = email.split('@')
        _, extension = server.split(".")
        if "edu" != extension:
            raise forms.ValidationError("Email debe tener extensión 'edu'")
        return email
    
    def clean_name(self):
        name = self.cleaned_data.get("name")
        return name

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
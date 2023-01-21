from django import forms

class RegisteredForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
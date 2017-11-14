from django import forms

class PatientRegistration(forms.Form):
    first_name = forms.CharField(label ='first_name')
from django import forms

class PatientRegistration(forms.Form):
    first_name = forms.CharField(label ='first_name')



class DocumentForm(forms.Form):
    imageFile = forms.FileField(
        label='Select a file',
    )
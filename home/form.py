from  django import forms
class form_data(forms.Form):
    name=forms.charfield(max_length=100)
    age=forms.intfield()

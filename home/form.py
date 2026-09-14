from  django import forms
class form_data(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()

from django.shortcuts import render
from .form import form_data
# Create your views here.
def detials(request):
    if request.method=="post":
        form1=form_data(request.post)
        if form1.is_valid():
            name=form1.cleaned_data["name"]
            age=form1.cleaned_data["age"]
            return render(request,"base.html",{
                "form1":form1,
                "name":name,
                "age":age
            })
    else:
        form1=form_data()
        return render(request,"base.html",{
            "form1":form1
        })
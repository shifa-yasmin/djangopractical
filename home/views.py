# from django.shortcuts import render
# from .form import form_data
# # Create your views here.
# def detials(request):
#     if request.method=="POST":
#         form1=form_data(request.POST)
#         if form1.is_valid():
#             name=form1.cleaned_data["name"]
#             age=form1.cleaned_data["age"]
#             return render(request,"base.html",{
#                 "form1":form1,
#                 "name":name,
#                 "age":age
#             })
#     else:
#         form1=form_data()
#         return render(request,"base.html",{
#             "form1":form1
#         


from django.shortcuts import render
def home(request):
    name="shifa",
    age=20
    return render(request,"base.html",{
        "name":name,
        "age":age
    })
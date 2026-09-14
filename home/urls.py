# from . import views
# from django.urls import path
# urlpatterns=[
#    path("",views.home,name="home"),
# ]


from . import views
from django.urls import path
urlpatterns=[
    path("",views.detials,name="form")
]
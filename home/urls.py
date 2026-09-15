# from . import views
# from django.urls import path
# urlpatterns=[
#    path("",views.home,name="home"),
# ]


# from . import views
# from django.urls import path
# urlpatterns=[
#     path("",views.detials,name="form")
# ]


from django.urls import path
from .views import home
urlpatterns=[
    path("",home)
]
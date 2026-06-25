from django.urls import path 

from . import views

urlpatterns = [
path('greet/', views.Greet),
path('', views.Home, name='home'),

            # GET page urls
path("getaddpage/",views.GetAdditionPage),
path("getsubpage/",views.GetSubtractionPage),
path("getmulpage/",views.GetMultiplicationPage),    
path("getdivpage/",views.GetDivisionPage),
path("gethomepage/",views.GetHomePage),   


            
            # airthamatic operation Urls

path("addition/", views.Addition),
path("subtraction/",views.Subtraction),
path("multiplication/", views.Multiplication),
path("division/", views.Division),
path("homepage/",views.HomePage), 

]
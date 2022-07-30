
from django.urls import path
from feedpanel import views
from django.urls import path,include

urlpatterns = [
   
    path('',views.home,name="home"),
    path('loanprediction',views.home,name="home"),
    path('aspect_analysis',views.aspect_analysis,name="aspect_analysis"),
   

]
from django.contrib import admin
from django.urls import path
from Shiva import views

urlpatterns = [
   path("",views.index,name='Lavanya'), 
   path("predict",views.predict,name='Predict'),
   path("about",views.about,name='Satpute'),
   path("login",views.login,name='login'),
   path("logout",views.logout,name='logout')
]
 
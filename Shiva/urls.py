from django.contrib import admin
from django.urls import path
from Shiva import views

urlpatterns = [
   path("info",views.index,name='info'), 
   path("predict",views.predict,name='Predict'),
   path("about",views.about,name='Satpute'),
   path("Register",views.Register,name='Register'),
   path("",views.signin,name='signin'),
   path("signin",views.signin,name='signin'),
   
]
 
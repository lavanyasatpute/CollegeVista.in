from django.contrib.auth import views as auth_views
from django.urls import path
from Shiva import views

urlpatterns = [
   path("info",views.index,name='info'), 
   path("predict",views.predict,name='Predict'),
   path("logout",views.logout,name='Satpute'),
   path("Register",views.Register,name='Register'),
   path("",views.signin,name='signin'),
   path("login",views.login,name='login'),
   path("signup",views.signup,name='signup'),
   path("pdf",views.pdf,name='pdf'),
   path("kit",views.kit,name="kit"),
   path('kitbranch',views.kitbranch,name='kitbranch'),
   path('branch',views.branch,name='branch'),
   
]
 
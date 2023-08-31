from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
   path('',views.index),
   path('j',views.inpage),
   path('demo/',views.demo),
   path('about/',views.about),
   path('services/',views.services),
   path('department/',views.department),
   path('doctors/',views.doctors),
   path('appointment/',views.appointment),
   path('contact/',views.contact),
   path('adminlogin/',views.adminloginform),
   path('adminreg/',views.adminreg),




   path('tb/',views.appointmentform),
   path('ct/',views.contactform),
   path('conview/',views.contactview),
   path('appointview/',views.appointmentview),

   #login
   path('login/',views.login),
   path('loging/',views.loginform),

   #logout
   path('logout/',views.logout),


   path('register/',views.register),
   path('registration/',views.registrationform),


   path('table/',views.table),
   path('appview/',views.appointtable),

   path('conup/',views.contactupdate),
   path('condelete/',views.contactdelete),
   path('appup/',views.appointmentupdate),
   path('appdelete/',views.appointmentdelet),



   #admin sides
   path('adminregister/',views.adminregistrationform),
   path('admindash/',views.admindash),
   path('adminloginform/',views.adminloginform),
   path('adminlogout/',views.adminlogout),

   path('allmembers/',views.allmembers),
   
   

  
]

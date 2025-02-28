from django.urls import path
from mcsapp import views
from django.urls import include

urlpatterns =[
  path('',views.reg,name="reg"),
  path('login/',views.login,name="login"),
  path('home/',views.home,name="home"),
  path('submit_complaint/',views.submit_complaint, name='submit_complaint'),
  path('analysis/',views.analysis,name="analysis"),
  path('logout/',views.user_logout,name="logout")
  






]
from django.urls import path
from . import views


urlpatterns =[
  path('',views.reg,name="reg"),
  path('login/',views.login,name="login"),
  path('home/',views.home,name="home"),
  path('submit_complaint/',views.submit_complaint, name='submit_complaint'),
  path('analysis/',views.analysis,name="analysis"),
  path('logout/',views.user_logout,name="logout"),
  path('view-complaints/', views.view_complaints, name='view_complaints'),
  path('mark-resolved/<int:complaint_id>/', views.mark_resolved, name='mark_resolved'),
  path('password_protect/', views.password_protect, name='password_protect'),
  path('view_complaints/', views.view_complaints, name='view_complaints'),
]
from django.urls import path
from.import views
appname = 'schooladmin'
urlpatterns=[
  path('home',views.home,name = 'admin_home'),
  path('change_password',views.change_password),
  path('add_teachers',views.add_teachers),
  path('view_teachers',views.view_teachers),

]  
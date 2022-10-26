from django.urls import path
from.import views
urlpatterns=[
  path('profile',views.profile),
  path('change_password',views.change_password),

]   
from django.urls import path
from.import views
urlpatterns=[
  path('admin_login',views.admin_login,name='admin_login'),
  path('product_home',views.product_home,name='product_home'),
  path('student_login',views.student_login,name='student_login'),
  path('teacher_login',views.teacher_login,name='teacher_login'),

]  
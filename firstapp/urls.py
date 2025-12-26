from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_product, name='add_product'),
    path('list/', views.product_list, name='product_list'),
    path('edit/<int:id>/', views.edit_product, name='edit_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),
    path('home', views.home, name='home'),
    path('signup/', views.usercreate, name='signup'),
    path('login/', views.loginpage, name='loginpage'),
    path('logout/', views.logout_user, name='logout'),
    path('about/', views.about, name='about'),
    path('', views.loginpage, name='loginpage'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutuser, name='logout'),
    path('home1/', views.home1, name='home1'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('edit_student/<int:id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),

    
    
]

from django.urls import path
from . import views
urlpatterns = [
    
    
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('signup_ad/', views.signup_ad, name='signup_ad'),
    path('signup_mod/', views.signup_mod, name='signup_mod'),
    path('signup_success/', views.signup_success, name='signup_success'),
    path('home_ad/', views.home_ad, name='home_ad'),
    path('home_mod/', views.home_mod, name='home_mod'),
    path('home_st/', views.home_st, name='home_st'),

]
from django.urls import path
from . import views

urlpatterns = [
    # Add your app's URL patterns here
    path('', views.login_, name='login_'),
    path('register/', views.register_, name='register_'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout/', views.logout_, name='logout_'),
]

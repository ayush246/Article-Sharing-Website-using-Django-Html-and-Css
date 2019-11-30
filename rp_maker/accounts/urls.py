from django.urls import path,include
from . import views
urlpatterns = [
    path('sign_up',views.sign_up,name="sign_up"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),    
]
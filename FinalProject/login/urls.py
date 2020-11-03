from django.urls import path
from .views import loginPageView, loggedinPageView

urlpatterns = [
    path('login/', loginPageView, name='login'),
    path("loggedin/", loggedinPageView, name="loggedin")
]
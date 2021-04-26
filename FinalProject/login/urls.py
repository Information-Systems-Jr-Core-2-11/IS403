from django.urls import path
from .views import loginPageView, loggedinPageView

urlpatterns = [
    path('', loginPageView, name='login'),
    path("loggedin/", loggedinPageView, name="loggedin")
]
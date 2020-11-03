from django.urls import path
from .views import signupPageView, signedupPageView

urlpatterns = [
    path('signup/', signupPageView, name='signup'),
    path("signedup/", signedupPageView, name="signedup")
]